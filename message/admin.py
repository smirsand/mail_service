from django.contrib import admin
from message.models import Newsletter, MailingMessage, MailingLog


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('get_clients', 'is_active', 'mailing_status', 'periodicity', 'start_date', 'end_date', 'start_time', 'end_time')
    verbose_name = 'Рассылка'
    verbose_name_plural = 'Рассылки'

    def get_clients(self, obj):
        return ", ".join([str(client.full_name) for client in obj.clients.all()])

    get_clients.short_description = 'Получатели'


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'content', 'status')
    verbose_name = 'Письмо'
    verbose_name_plural = 'Письма'


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'status', 'newsletter')
    verbose_name = 'Лог'
    verbose_name_plural = 'Логи'
