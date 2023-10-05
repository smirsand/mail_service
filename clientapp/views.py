from django.views.generic import ListView

from clientapp.models import Client


class ClientListView(ListView):
    """
    Контроллер для просмотра клиентов.
    """
    model = Client
    template_name = 'clientapp/clientapp_list.html'
