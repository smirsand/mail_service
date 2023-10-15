from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'count_views', 'publication_date')
    verbose_name = 'Блог'
    verbose_name_plural = 'Блог'
