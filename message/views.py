from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from client.models import Client
from message.forms import NewsletterForm
from message.models import Newsletter, MailingLog, MailingMessage


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер для создания рассылок.
    """
    model = Newsletter
    form_class = NewsletterForm
    template_name = 'message/newsletter_form.html'
    success_url = reverse_lazy('message:list_newsletter')


class NewsletterUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Контроллер для редактирования рассылок.
    """
    model = Newsletter
    form_class = NewsletterForm
    permission_required = 'message.change_newsletter'
    template_name = 'message/newsletter_form.html'
    success_url = reverse_lazy('message:list_newsletter')


class NewsletterListView(LoginRequiredMixin, ListView):
    """
    Контроллер для просмотра рассылок.
    """
    model = Newsletter
    template_name = 'message/newsletter_list.html'

    def get_queryset(self):

        user = self.request.user

        if user.is_active:
            queryset = super().get_queryset()
        else:
            try:
                client = Client.objects.get(user=user)
                queryset = super().get_queryset().filter(client=client)
            except Client.DoesNotExist:
                queryset = super().get_queryset().none()

        return queryset


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


class MailingMessageCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер для создания письма.
    """
    model = MailingMessage
    template_name = 'message/newsletter_form.html'
    fields = ('subject', 'content',)
    success_url = reverse_lazy('message:list_mailingmessage')


class MailingMessageListView(LoginRequiredMixin, ListView):
    """
    Контроллер для просмотра писем.
    """
    model = MailingMessage
    template_name = 'message/message_list.html'


class MailingMessageDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер для просмотра письма.
    """
    model = MailingMessage
    template_name = 'message/message_detail.html'


class MailingMessageUpdateView(LoginRequiredMixin, UpdateView):
    """
    Контроллер для редактирования писем.
    """
    model = MailingMessage
    fields = ('subject', 'content',)
    template_name = 'message/message_form.html'
    success_url = reverse_lazy('message:list_mailingmessage')


class MailingMessageDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контроллер для удаления письма.
    """
    model = MailingMessage
    template_name = 'message/message_confirm_delete.html'
    success_url = reverse_lazy('message:list_mailingmessage')