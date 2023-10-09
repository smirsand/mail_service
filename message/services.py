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
