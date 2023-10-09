from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from client.forms import ClientForm
from client.models import Client


class ClientListView(ListView):
    """
    Контроллер для просмотра клиентов.
    """
    model = Client
    template_name = 'client/client_list.html'


class ClientCreateView(CreateView):
    """
    Контроллер для создания рассылок.
    """
    model = Client
    form_class = ClientForm
    template_name = 'client/client_form.html'
    success_url = reverse_lazy('client:list_client')


class ClientDetailView(DetailView):
    """
    Контроллер для просмотра карточки клиента.
    """

    model = Client
    template_name = 'client/client_detail.html'


class ClientUpdateView(UpdateView):
    """
    Контроллер для редактирования карточки клиента.
    """

    model = Client
    form_class = ClientForm
    template_name = 'client/client_form.html'
    success_url = reverse_lazy('client:list_client')


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client/client_confirm_delete.html'
    success_url = reverse_lazy('client:list_client')