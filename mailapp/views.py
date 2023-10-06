from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from mailapp.forms import NewsletterForm
from mailapp.models import Newsletter


class NewsletterListView(ListView):
    """
    Контроллер для просмотра рассылок.
    """
    model = Newsletter
    template_name = 'mailapp/mailapp_list.html'


class NewsletterCreateView(CreateView):
    """
    Контроллер для создания рассылок.
    """
    model = Newsletter
    form_class = NewsletterForm
    template_name = 'mailapp/mailapp_form.html'
    success_url = reverse_lazy('clientapp:clientapp_list')


class NewsletterUpdateView(UpdateView):
    pass