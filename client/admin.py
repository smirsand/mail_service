from django.contrib import admin

from client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    list_filter = ('full_name',)
    verbose_name = 'Клиенты'

