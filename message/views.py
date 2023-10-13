from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from client.models import Client
from message.forms import NewsletterForm
from message.models import Newsletter, MailingLog


class NewsletterCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Контроллер для создания рассылок.
    """
    model = Newsletter
    form_class = NewsletterForm
    permission_required = 'message.create_newsletter'
    template_name = 'message/newsletter_form.html'
    success_url = reverse_lazy('message:list_newsletter')

    # def form_valid(self, form):
    #     newsletter_object = form.save(commit=False)
    #     newsletter_object.clients = self.request.user
    #     newsletter_object.save()
    #
    #     return super().form_valid(form)


class NewsletterUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Контроллер для редактирования рассылок.
    """
    model = Newsletter
    form_class = NewsletterForm
    permission_required = 'message.update_newsletter'
    template_name = 'message/newsletter_form.html'
    success_url = reverse_lazy('message:list_newsletter')

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if self.object.clients != self.request.user and not self.request.user.is_staff:
    #         raise Http404
    #     return self.object


class NewsletterListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    Контроллер для просмотра рассылок.
    """
    model = Newsletter
    permission_required = 'message.view_newsletter'
    template_name = 'message/newsletter_list.html'

    def get_queryset(self):
        # Получаем текущего пользователя
        user = self.request.user

        if user.is_superuser:
            # Если пользователь является суперпользователем, показываем все рассылки
            queryset = super().get_queryset()
        else:
            # Фильтруем рассылки по клиентам, связанным с пользователем
            try:
                client = Client.objects.get(user=user)
                queryset = super().get_queryset().filter(client=client)
            except Client.DoesNotExist:
                queryset = super().get_queryset().none()

        return queryset

    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #     client_pk = self.kwargs.get('pk')
    #     context_data['newsletter'] = self.model.objects.filter(clients=client_pk)
    #     return context_data

    # def get_queryset(self):
    #     queryset = super().get_queryset().filter(
    #         id=self.kwargs.get('pk'),
    #     )
    #
    #     if not self.request.user.is_staff:
    #        queryset = queryset.filter(clients=self.request.user)
    #
    #     return queryset


class NewsletterDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """
    Контроллер для просмотра рассылки.
    """
    model = Newsletter
    permission_required = 'message.view_newsletter'
    template_name = 'message/newsletter_detail.html'


class NewsletterDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Контроллер для удаления рассылки.
    """
    model = Newsletter
    permission_required = 'message.delete_newsletter'
    template_name = 'message/newsletter_confirm_delete.html'
    success_url = reverse_lazy('message:list_newsletter')


class MailingLogListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    Контроллер для просмотра списка логов.
    """
    model = MailingLog
    permission_required = 'message.view_mailinglog'
    template_name = 'message/log_list.html'


def toggle_active_newsletter(request, pk):
    newsletter_item = get_object_or_404(Newsletter, pk=pk)
    if newsletter_item.is_active:
        newsletter_item.is_active = False
    else:
        newsletter_item.is_active = True

    newsletter_item.save()

    return redirect(reverse('message:list_newsletter'))
