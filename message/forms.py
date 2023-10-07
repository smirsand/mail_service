from django import forms

from message.models import Newsletter, MailingMessage


class NewsletterForm(forms.ModelForm):
    """Форма создания рассылки."""
    message = forms.ModelChoiceField(queryset=MailingMessage.objects.all(), empty_label='Выберите сообщение',
                                     label='Сообщение')

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
