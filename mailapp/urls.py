from django.urls import path

from mailapp.apps import MailappConfig
from mailapp.views import NewsletterListView

app_name = MailappConfig.name

urlpatterns = [
    path('mailapp_list', NewsletterListView.as_view(), name='mailapp_list')
]
