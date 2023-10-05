from django.db import models

from clientapp.models import Client


class Newsletter(models.Model):
    """
    Рассылка
    """
    FREQUENCY_CHOICES = [
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
        ('monthly', 'Ежемесячно'),
    ]

    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    ]

    mailing_time = models.DateTimeField(verbose_name='время рассылки', blank=True, null=True)
    periodicity = models.CharField(choices=FREQUENCY_CHOICES, verbose_name='периодичность')
    mailing_status = models.CharField(max_length=100, choices=STATUS_CHOICES, verbose_name='статус рассылки')
    recipient = models.ManyToManyField(Client, related_name='newsletters', verbose_name='получатели')

    def __str__(self):
        return self.mailing_status

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class MailingMessage(models.Model):
    """
    Письма
    """
    subject = models.CharField(max_length=100, verbose_name='тема письма')
    content = models.TextField(verbose_name='тело письма')
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, null=True, related_name='messages',
                                   verbose_name='рассылка')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'


class MailingLog(models.Model):
    """
    Лог
    """
    date = models.DateField(auto_now_add=True, verbose_name='дата попытки')
    time = models.TimeField(auto_now_add=True, verbose_name='время попытки')
    attempt_status = models.BooleanField(default=False, verbose_name='статус попытки')
    server_response = models.TextField(verbose_name='ответ сервера')
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='logs', verbose_name='рассылка')
    message = models.ForeignKey(MailingMessage, on_delete=models.CASCADE, default=0, related_name='logs',
                                verbose_name='письмо')

    def __str__(self):
        return self.attempt_status

    class Meta:
        verbose_name = 'лог рассылки'
        verbose_name_plural = 'лог рассылок'

