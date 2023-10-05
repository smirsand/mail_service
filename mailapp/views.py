from django.views.generic import ListView

from mailapp.models import Newsletter


class NewsletterListView(ListView):
    """
    Контроллер для просмотра рассылок.
    """
    model = Newsletter
    template_name = 'mailapp/mailapp_list.html'
