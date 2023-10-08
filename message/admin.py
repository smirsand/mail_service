from django.contrib import admin
from message.models import Newsletter, MailingMessage, MailingLog


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('get_mailing_time', 'periodicity', 'mailing_status')
    verbose_name = 'Рассылка'

    def get_mailing_time(self, obj):
        return obj.mailing_time.strftime('%Y-%m-%d %H:%M:%S')

    get_mailing_time.short_description = 'Время рассылки'


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'content')
    verbose_name = 'Письмо'


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'success', 'newsletter')
    verbose_name = 'Лог'
