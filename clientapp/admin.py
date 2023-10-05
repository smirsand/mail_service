from django.contrib import admin

from clientapp.models import Client


@admin.register(Client)
class ClientappAdmin(admin.ModelAdmin):
    list_display = ('name',)
    verbose_name = 'Клиенты'

