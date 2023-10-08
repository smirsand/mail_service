from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from message.forms import NewsletterForm
from message.models import Newsletter


class NewsletterCreateView(CreateView):
    """
    Контроллер для создания рассылок.
    """
    model = Newsletter
    form_class = NewsletterForm
    template_name = 'message/newsletter_form.html'
    success_url = reverse_lazy('message:list_newsletter')

    def get_form(self, form_class=None):
        # Выводим значения, передаваемые в поле `periodicity`
        form = super().get_form(form_class)
        print(form.fields['periodicity'].choices)
        return form


class NewsletterUpdateView(UpdateView):
    """
    Контроллер для редактирования рассылок.
    """
    model = Newsletter
    form_class = NewsletterForm
    template_name = 'message/newsletter_form.html'
    success_url = reverse_lazy('message:list_newsletter')

    def get_form(self, form_class=None):
        # Выводим значения, передаваемые в поле `periodicity`
        form = super().get_form(form_class)
        print(form.fields['periodicity'].choices)
        return form


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
