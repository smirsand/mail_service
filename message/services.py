import datetime
import random
from smtplib import SMTPException

from django.core.cache import cache
from django.http import BadHeaderError
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from message.models import Newsletter, MailingMessage, MailingLog
from users.models import User
from datetime import datetime, timedelta


def send_email(client, mailing, message):
    try:
        result = send_mail(
            subject=message.subject,
            message=message.content,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client.email],
            fail_silently=False,
        )

        MailingLog.objects.create(
            newsletter=mailing,
            client=client,
            status=MailingLog.STATUS_OK,
        )

    except BadHeaderError as e:
        print("Произошла ошибка BadHeaderError при отправке письма:", str(e))
        MailingLog.objects.create(
            newsletter=mailing,
            client=client,
            status=MailingLog.STATUS_FAILED,
            server_response="BadHeaderError: " + str(e),
        )

    except SMTPException as e:
        print("Произошла ошибка SMTP при отправке письма:", str(e))
        MailingLog.objects.create(
            newsletter=mailing,
            client=client,
            status=MailingLog.STATUS_FAILED,
            server_response="SMTPException: " + str(e),
        )


def send_mails():

    now_time = timezone.localtime(timezone.now()).time()

    for mailing in Newsletter.objects.all().filter(mailing_status=Newsletter.STARTED):

        if mailing.start_time <= now_time < mailing.end_time:

            for mailing_client in mailing.clients.all():

                message = MailingMessage.objects.filter(newsletter=mailing, status=MailingMessage.SEND).first()

                if message is None:
                    return

                log = MailingLog.objects.filter(
                    client=mailing_client,
                    newsletter=mailing
                )

                if log.exists():
                    last_try_date = log.order_by('-time').first().time
                    last_try_datetime = datetime.combine(datetime.now().date(), last_try_date)

                    now = timezone.localtime(timezone.now()).replace(tzinfo=last_try_datetime.tzinfo)

                    if mailing.periodicity == timedelta(days=1):
                        if (now - last_try_datetime) >= timedelta(days=1):
                            send_email(mailing_client, mailing, message)

                    elif mailing.periodicity == timedelta(weeks=1):
                        if (now - last_try_datetime) >= timedelta(weeks=1):
                            send_email(mailing_client, mailing, message)

                    elif mailing.periodicity == timedelta(days=30):
                        if (now - last_try_datetime) >= timedelta(days=30):
                            send_email(mailing_client, mailing, message)

                else:
                    send_email(mailing_client, mailing, message)

            message.status = MailingMessage.SENT
            message.save()


def send_new_password(email, new_password):
    send_mail(
        subject='Вы сменили пароль!',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )


def send_for_confirmation(user_pk):
    user = User.objects.get(pk=user_pk)

    send_mail(
        subject='Вы зарегистрировали на сайте управления рассылками',
        message=f'Добро пожаловать на наш сайт! Пожалуйста, подтвердите вашу почту. Проверочный код: {user.code}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=False
    )


def generate_confirmation_password():
    """
    Генерация пароля подтверждения.
    """
    password_confirmation = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    return password_confirmation
