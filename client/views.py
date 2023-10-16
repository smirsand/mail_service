from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from blog.models import Blog
from client.forms import ClientForm
from client.models import Client
from message.models import Newsletter


def home(request):
    """
    Контроллер главной страницы.
    """
    template_name = 'client/home.html'
    total_newsletters = Newsletter.objects.count()
    active_newsletters = Newsletter.objects.filter(is_active=True).count()
    unique_clients = Newsletter.objects.values('clients').distinct().count()
    random_articles = Blog.objects.order_by('?')[:3]

    context = {
        'total_newsletters': total_newsletters,
        'active_newsletters': active_newsletters,
        'unique_clients': unique_clients,
        'random_articles': random_articles,
    }

    return render(request, template_name, context)


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
    """
    Контроллер для удаления карточки клиента.
    """
    model = Client
    permission_required = 'client.delete_client'
    template_name = 'client/client_confirm_delete.html'
    success_url = reverse_lazy('client:list_client')
