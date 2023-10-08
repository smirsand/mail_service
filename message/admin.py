from django.contrib import admin
from message.models import Newsletter, MailingMessage, MailingLog


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('mailing_status', 'periodicity', 'mailing_status')
    verbose_name = 'Рассылка'


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'content')
    verbose_name = 'Письмо'


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'success', 'newsletter')
    verbose_name = 'Лог'
