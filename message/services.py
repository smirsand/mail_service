from django.conf import settings
from django.core.mail import send_mail
from message.models import MailingLog


def send_mail_custom(message_item):
    for client in message_item.clients.all():  # Получить адреса получателей
        send_mail(
            f'{message_item.message.subject}',
            f'{message_item.message.content}',
            settings.EMAIL_HOST_USER,
            [client.email],
            fail_silently=False
        )

    log = MailingLog(
        status=MailingLog.STATUS_OK,
        newsletter=message_item
    )
    log.save()

    return log


def send_new_password(email, new_password):
    send_mail(
        subject='Вы сменили пароль!',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
