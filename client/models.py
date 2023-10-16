from django.db import models

from users.models import User


class Client(models.Model):
    """
    Модель клиента.
    """
    email = models.EmailField(verbose_name='почта', unique=True)
    full_name = models.CharField(max_length=150, default='', verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=5, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.full_name} {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'