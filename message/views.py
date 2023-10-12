from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from message.forms import NewsletterForm
from message.models import Newsletter, MailingLog


class NewsletterCreateView(CreateView):
    """
    Контроллер для создания рассылок.
    """
    model = Newsletter
    form_class = NewsletterForm
    template_name = 'message/newsletter_form.html'
    success_url = reverse_lazy('message:list_newsletter')


class NewsletterUpdateView(UpdateView):
    """
    Контроллер для редактирования рассылок.
    """
    model = Newsletter
    form_class = NewsletterForm
    template_name = 'message/newsletter_form.html'
    success_url = reverse_lazy('message:list_newsletter')


class NewsletterListView(ListView):
    """
    Контроллер для просмотра рассылок.
    """
    model = Newsletter
    template_name = 'message/newsletter_list.html'


class NewsletterDetailView(DetailView):
    """
    Контроллер для просмотра рассылки.
    """
    model = Newsletter
    template_name = 'message/newsletter_detail.html'


class NewsletterDeleteView(DeleteView):
    """
    Контроллер для удаления рассылки.
    """
    model = Newsletter
    template_name = 'message/newsletter_confirm_delete.html'
    success_url = reverse_lazy('message:list_newsletter')


class MailingLogListView(ListView):
    """
    Контроллер для просмотра списка логов.
    """
    model = MailingLog
    template_name = 'message/log_list.html'
