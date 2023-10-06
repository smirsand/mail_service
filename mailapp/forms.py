from django import forms

from mailapp.models import Newsletter


class NewsletterForm(forms.ModelForm):
    """Форма создания и редактирования рассылки."""

    class Meta:
        model = Newsletter
        fields = '__all__'
        labels = {
            'mailing_time': 'Время рассылки',
            'periodicity': 'Периодичность',
            'mailing_status': 'Статус рассылки',
            'recipient': 'Получатели',
        }
        widgets = {
            'mailing_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
