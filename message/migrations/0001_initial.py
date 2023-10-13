# Generated by Django 4.2.6 on 2023-10-13 10:58

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('К отправке', 'К отправке'), ('Отправлено', 'Отправлено')], default='К отправке', max_length=50, verbose_name='статус отправки')),
                ('subject', models.CharField(max_length=100, verbose_name='тема письма')),
                ('content', models.TextField(verbose_name='тело письма')),
            ],
            options={
                'verbose_name': 'сообщение для рассылки',
                'verbose_name_plural': 'сообщения для рассылки',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='дата начала рассылки')),
                ('end_date', models.DateField(default=datetime.date(2023, 12, 31), verbose_name='дата окончания рассылки')),
                ('start_time', models.TimeField(default=datetime.time(14, 0), verbose_name='время начала рассылки')),
                ('end_time', models.TimeField(default=datetime.time(15, 0), verbose_name='время окончания рассылки')),
                ('periodicity', models.DurationField(choices=[(datetime.timedelta(days=1), 'Ежедневно'), (datetime.timedelta(days=7), 'Еженедельно'), (datetime.timedelta(days=30, seconds=43200), 'Ежемесячно')], default=datetime.timedelta(days=1), max_length=20, verbose_name='периодичность')),
                ('mailing_status', models.CharField(choices=[('Завершена', 'Завершена'), ('Создана', 'Создана'), ('Запущена', 'Запущена')], default='Создана', max_length=100, verbose_name='статус рассылки')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
            },
        ),
        migrations.CreateModel(
            name='MailingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='дата попытки')),
                ('time', models.TimeField(auto_now_add=True, verbose_name='время попытки')),
                ('status', models.CharField(choices=[('ok', 'Успешно'), ('failed', 'Ошибка')], default='Успешно', max_length=20, verbose_name='статус')),
                ('server_response', models.TextField(blank=True, verbose_name='ответ сервера')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mailing_logs', to='client.client', verbose_name='клиент')),
                ('newsletter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='message.newsletter', verbose_name='рассылка')),
            ],
            options={
                'verbose_name': 'лог',
                'verbose_name_plural': 'логи',
            },
        ),
    ]
