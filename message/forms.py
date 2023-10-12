from django import forms

from message.models import Newsletter, MailingMessage


class NewsletterForm(forms.ModelForm):
    """Форма создания рассылки."""
    message = forms.ModelChoiceField(queryset=MailingMessage.objects.all(), empty_label='Выберите сообщение',
                                     label='Сообщение')


    class Meta:
        model = Newsletter
        fields = '__all__'

        widgets = {
            'mailing_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
