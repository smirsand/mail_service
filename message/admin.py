from django.contrib import admin

from message.models import Newsletter, MailingMessage, MailingLog


@admin.register(Newsletter)
class MailappAdmin(admin.ModelAdmin):
    list_display = ('mailing_time', 'periodicity', 'mailing_status',)
    verbose_name = 'Рассылки'


@admin.register(MailingMessage)
class MailappAdmin(admin.ModelAdmin):
    list_display = ('subject', 'content',)
    verbose_name = 'Письма'


@admin.register(MailingLog)
class MailappAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'attempt_status', 'server_response',)
    verbose_name = 'Лог'