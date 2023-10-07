from django.views.generic import ListView

from client.models import Client


class ClientListView(ListView):
    """
    Контроллер для просмотра клиентов.
    """
    model = Client
    template_name = 'client/client_list.html'
