# Generated by Django 4.2.6 on 2023-10-13 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_mailingmessage_newsletter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'permissions': [('is_active', 'Can block рассылки')], 'verbose_name': 'рассылка', 'verbose_name_plural': 'рассылки'},
        ),
    ]
