from django.contrib import admin

from client.models import Client


@admin.register(Client)
class ClientappAdmin(admin.ModelAdmin):
    list_display = ('name',)
    verbose_name = 'Клиенты'

