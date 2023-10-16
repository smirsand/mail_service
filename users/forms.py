from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    """
    Форма регистрации пользователя.
    """

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    """
    Форма профиля пользователя
    """

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()  # Скрывает поле password в форме.


class UserVerificationForm(forms.Form):
    """
    Форма верификации пользователя.
    """
    code = forms.CharField(max_length=6, min_length=6)
