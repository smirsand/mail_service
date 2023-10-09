from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from message.forms import NewsletterForm
from message.models import Newsletter, MailingLog
from message.services import send_mail_custom


class NewsletterCreateView(CreateView):
    """
    Контроллер для создания рассылок.
    """
    model = Newsletter
    form_class = NewsletterForm
    template_name = 'message/newsletter_form.html'
    success_url = reverse_lazy('message:list_newsletter')

    def form_valid(self, form):
        obj = form.save()
        send_mail_custom(obj)
        return super().form_valid(form)


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
    model = Newsletter
    template_name = 'message/newsletter_confirm_delete.html'
    success_url = reverse_lazy('message:list_newsletter')


class MailingLogListView(ListView):
    model = MailingLog
    template_name = 'message/mailinglog_list.html'


class MailingLogDetailView(DetailView):
    model = MailingLog
    template_name = 'message/mailinglog_detail.html'
