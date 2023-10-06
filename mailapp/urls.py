from django.urls import path

from mailapp.apps import MailappConfig
from mailapp.views import NewsletterListView, NewsletterCreateView, NewsletterUpdateView

app_name = MailappConfig.name

urlpatterns = [
    path('mailapp_list', NewsletterListView.as_view(), name='mailapp_list'),
    path('create', NewsletterCreateView.as_view(), name='create_newsletter'),
    # path('update/<int:pk>/', NewsletterUpdateView.as_view(), name='mailapp_form')
]
