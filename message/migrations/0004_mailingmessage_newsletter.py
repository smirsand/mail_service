# Generated by Django 4.2.6 on 2023-10-13 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_remove_mailingmessage_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailingmessage',
            name='newsletter',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='message.newsletter', verbose_name='рассылка'),
        ),
    ]
