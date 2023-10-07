from django.urls import path

from client.apps import ClientConfig
from client.views import ClientListView

app_name = ClientConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='list_client'),
]
