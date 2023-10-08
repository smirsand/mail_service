from django.urls import path

from message.apps import MessageConfig
from message.views import NewsletterListView, NewsletterCreateView, NewsletterDeleteView, NewsletterDetailView, \
    NewsletterUpdateView

app_name = MessageConfig.name

urlpatterns = [
    path('list/', NewsletterListView.as_view(), name='list_newsletter'),
    path('create/', NewsletterCreateView.as_view(), name='create_newsletter'),
    path('update/<int:pk>/', NewsletterUpdateView.as_view(), name='update_newsletter'),
    path('detail/<int:pk>/', NewsletterDetailView.as_view(), name='detail_newsletter'),
    path('delete/<int:pk>/', NewsletterDeleteView.as_view(), name='delete_newsletter'),
]
