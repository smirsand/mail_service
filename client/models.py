from django.db import models


class Client(models.Model):
    """
    Клиент
    """
    email = models.EmailField(verbose_name='почта', unique=True)
    name = models.CharField(max_length=100, verbose_name='имя')
    surname = models.CharField(max_length=100, verbose_name='фамилия')
    patronymic = models.CharField(max_length=100, verbose_name='отчество', blank=True, null=True)
    comment = models.TextField(verbose_name='комментарий', blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
