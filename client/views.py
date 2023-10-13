from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from client.forms import ClientForm
from client.models import Client


class ClientListView(LoginRequiredMixin, ListView):
    """
    Контроллер для просмотра клиентов.
    """
    model = Client
    template_name = 'client/client_list.html'


class ClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Контроллер для создания рассылок.
    """
    model = Client
    form_class = ClientForm
    permission_required = 'client.add_client'
    template_name = 'client/client_form.html'
    success_url = reverse_lazy('client:list_client')


class ClientDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер для просмотра карточки клиента.
    """

    model = Client
    template_name = 'client/client_detail.html'


class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Контроллер для редактирования карточки клиента.
    """

    model = Client
    form_class = ClientForm
    permission_required = 'client.change_client'
    template_name = 'client/client_form.html'
    success_url = reverse_lazy('client:list_client')


class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    permission_required = 'client.delete_client'
    template_name = 'client/client_confirm_delete.html'
    success_url = reverse_lazy('client:list_client')