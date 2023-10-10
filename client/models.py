from django.db import models


class Client(models.Model):
    """
    Клиент
    """
    email = models.EmailField(verbose_name='почта', unique=True)
    full_name = models.CharField(max_length=150, default='', verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий', blank=True, null=True)

    def __str__(self):
        return f'{self.full_name} {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'