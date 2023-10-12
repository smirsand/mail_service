from datetime import timedelta, date
from django.db import models
from datetime import time
from django.utils import timezone
from client.models import Client


class Newsletter(models.Model):
    """
    Рассылка
    """

    DAILY = timedelta(days=1)
    WEEKLY = timedelta(days=7)
    MONTHLY = timedelta(days=30, hours=12)

    FREQUENCY_CHOICES = [
        (DAILY, 'Ежедневно'),
        (WEEKLY, 'Еженедельно'),
        (MONTHLY, 'Ежемесячно'),
    ]

    CREATED = 'Создана'
    STARTED = 'Запущена'
    COMPLETED = 'Завершена'

    STATUS_CHOICES = [
        (COMPLETED, "Завершена"),
        (CREATED, "Создана"),
        (STARTED, "Запущена"),
    ]

    start_date = models.DateField(verbose_name='дата начала рассылки', default=timezone.now)
    end_date = models.DateField(verbose_name='дата окончания рассылки', default=date(2023, 12, 31))
    start_time = models.TimeField(verbose_name='время начала рассылки', default=time(hour=14))
    end_time = models.TimeField(verbose_name='время окончания рассылки', default=time(hour=15))
    periodicity = models.DurationField(max_length=20, choices=FREQUENCY_CHOICES, default=DAILY,
                                       verbose_name='периодичность')
    mailing_status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=CREATED,
                                      verbose_name='статус рассылки')
    clients = models.ManyToManyField(Client, related_name='newsletters', verbose_name='получатели')

    def clients_list(self):
        return ", ".join([str(client.full_name) for client in self.clients.all()])  # Обновленный код

    def __str__(self):
        return f'Рассылка {self.id} - {self.mailing_status}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class MailingMessage(models.Model):
    """
    Сообщение для рассылки
    """
    SEND = 'К отправке'
    SENT = 'Отправлено'

    STATUS_CHOICES = [
        (SEND, "К отправке"),
        (SENT, "Отправлено"),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=SEND, verbose_name='статус отправки')
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='messages',
                                   default=Newsletter.objects.first(), verbose_name='рассылка')
    subject = models.CharField(max_length=100, verbose_name='тема письма')
    content = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'сообщение для рассылки'
        verbose_name_plural = 'сообщения для рассылки'


class MailingLog(models.Model):
    """
    Лог рассылки
    """
    STATUS_OK = 'ok'
    STATUS_FAILED = 'failed'

    STATUSES = (
        (STATUS_OK, 'Успешно'),
        (STATUS_FAILED, 'Ошибка'),
    )

    date = models.DateField(auto_now_add=True, verbose_name='дата попытки')
    time = models.TimeField(auto_now_add=True, verbose_name='время попытки')
    status = models.CharField(max_length=20, choices=STATUSES, verbose_name='статус')
    server_response = models.TextField(verbose_name='ответ сервера', blank=True)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='logs', verbose_name='рассылка')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент',
                               related_name='mailing_logs', blank=True, null=True)

    def __str__(self):
        if self.status == MailingLog.STATUS_OK:
            return f'Лог {self.id} - Успешно'
        elif self.status == MailingLog.STATUS_FAILED:
            return f'Лог {self.id} - Не успешно'
        else:
            return f'Лог {self.id} - Неизвестный статус'

    class Meta:
        verbose_name = 'лог рассылки'
        verbose_name_plural = 'логи рассылки'