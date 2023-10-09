from django.urls import path

from client.apps import ClientConfig
from client.views import ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView

app_name = ClientConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='list_client'),
    path('create/', ClientCreateView.as_view(), name='create_client'),
    path('detail/<int:pk>/', ClientDetailView.as_view(), name='detail_client'),
    path('update/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
]
