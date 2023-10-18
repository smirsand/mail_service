from django.urls import path

from message.apps import MessageConfig
from message.views import NewsletterListView, NewsletterCreateView, NewsletterDeleteView, NewsletterDetailView, \
    NewsletterUpdateView, MailingLogListView, toggle_active_newsletter, MailingMessageCreateView, \
    MailingMessageListView, MailingMessageDetailView, MailingMessageUpdateView, MailingMessageDeleteView

app_name = MessageConfig.name

urlpatterns = [
    path('list/', NewsletterListView.as_view(), name='list_newsletter'),
    path('create/', NewsletterCreateView.as_view(), name='create_newsletter'),
    path('update/<int:pk>/', NewsletterUpdateView.as_view(), name='update_newsletter'),
    path('detail/<int:pk>/', NewsletterDetailView.as_view(), name='detail_newsletter'),
    path('delete/<int:pk>/', NewsletterDeleteView.as_view(), name='delete_newsletter'),
    path('list_log/', MailingLogListView.as_view(), name='list_mailing_log'),
    path('activity/<int:pk>/', toggle_active_newsletter, name='toggle_active_newsletter'),
    path('create_mailingmessage/', MailingMessageCreateView.as_view(), name='create_mailingmessage'),
    path('list_mailingmessage/', MailingMessageListView.as_view(), name='list_mailingmessage'),
    path('detail_mailingmessage/<int:pk>/', MailingMessageDetailView.as_view(), name='detail_mailingmessage'),
    path('update_mailingmessage/<int:pk>/', MailingMessageUpdateView.as_view(), name='update_mailingmessage'),
    path('delete_mailingmessage/<int:pk>/', MailingMessageDeleteView.as_view(), name='delete_mailingmessage'),
]
