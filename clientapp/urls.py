from django.urls import path

from clientapp.apps import ClientappConfig
from clientapp.views import ClientListView

app_name = ClientappConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='clientapp_list'),
]
