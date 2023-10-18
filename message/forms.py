from django import forms

from message.models import Newsletter, MailingMessage


class NewsletterForm(forms.ModelForm):
    """Форма создания рассылки."""

    class Meta:
        model = Newsletter
        fields = '__all__'

        widgets = {
            'mailing_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class MailingMessageForm(forms.ModelForm):
    """Форма создания рассылки."""

    class Meta:
        model = MailingMessage
        fields = '__all__'