from django import forms

from client.models import Client


class ClientForm(forms.ModelForm):
    """
    Форма создания клиента.
    """

    class Meta:
        model = Client
        fields = '__all__'
