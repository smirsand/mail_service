from smtplib import SMTPException

from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

from message.models import Newsletter, MailingMessage, MailingLog


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
            status=result,
        )

        if result == 1:
            print("Письмо успешно отправлено")
        else:
            print("Ошибка отправки письма")

    except SMTPException as e:
        print("Произошла ошибка SMTP при отправке письма:", str(e))


def send_mails():
    now = timezone.now()
    now_time = now.time()

    for mailing in Newsletter.objects.filter(mailing_status=Newsletter.STARTED):
        if mailing.start_date <= now.date() <= mailing.end_date and mailing.start_time < now_time < mailing.end_time:
            for mailing_client in mailing.clients.all():
                if mailing_client is not None:  # Проверка, что клиент существует
                    message = mailing.message

                    if message.status == MailingMessage.SEND:  # Проверка, что сообщение пригодно к отправке
                        log = MailingLog.objects.filter(newsletter=mailing, client=mailing_client)

                        if log.exists():
                            last_try_date = log.order_by('-time').first().time

                            if mailing.periodicity == Newsletter.DAILY:
                                if (now.date() - last_try_date.date()) >= Newsletter.DAILY:
                                    send_email(mailing_client, mailing, message)

                            elif mailing.periodicity == Newsletter.WEEKLY:
                                if (now.date() - last_try_date.date()) >= Newsletter.WEEKLY:
                                    send_email(mailing_client, mailing, message)

                            elif mailing.periodicity == Newsletter.MONTHLY:
                                if (now.date() - last_try_date.date()) >= Newsletter.MONTHLY:
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
