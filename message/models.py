from datetime import timedelta

from django.db import models
from datetime import time

from client.models import Client


class MailingMessage(models.Model):
    """
    Сообщение для рассылки
    """
    subject = models.CharField(max_length=100, verbose_name='тема письма')
    content = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'сообщение для рассылки'
        verbose_name_plural = 'сообщения для рассылки'


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
        (CREATED, 'Создана'),
        (STARTED, 'Запущена'),
        (COMPLETED, 'Завершена'),
    ]

    start_time = models.TimeField(verbose_name='время начала рассылки', default=time(hour=14))
    end_time = models.TimeField(verbose_name='время окончания рассылки', default=time(hour=15))
    periodicity = models.DurationField(max_length=20, choices=FREQUENCY_CHOICES, default=DAILY,
                                       verbose_name='периодичность')
    mailing_status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=CREATED,
                                      verbose_name='статус рассылки')
    clients = models.ManyToManyField(Client, related_name='newsletters', verbose_name='получатели')
    message = models.ForeignKey(MailingMessage, on_delete=models.CASCADE, related_name='newsletters',
                                verbose_name='сообщение')

    def __str__(self):
        return f'Рассылка {self.id} - {self.mailing_status}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


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
    newsletter = models.OneToOneField(Newsletter, on_delete=models.CASCADE, related_name='logs',
                                      verbose_name='рассылка')

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
