import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from message.services import send_new_password, generate_confirmation_password, send_for_confirmation
from users.forms import UserRegisterForm, UserProfileForm, UserVerificationForm
from users.models import User


class RegisterView(CreateView):
    """
    Контроллер регистрации пользователя.
    """
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def get_success_url(self):
        return reverse('users:verification', args=[self.object.pk])

    def form_valid(self, form):
        new_user = form.save()
        new_user.code = generate_confirmation_password()
        new_user.save()

        send_for_confirmation(new_user.pk)

        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, UpdateView):
    """
    Контроллер редактирования пользователя.
    """
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    """
    Генерация нового пароля.
    """
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    request.user.set_password(new_password)
    request.user.save()
    send_new_password(request.user.email, new_password)
    return redirect(reverse('client:list_client'))


def pass_verification(request, pk):
    """
    Подтверждает активацию пользователя после регистрации.
    """
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = UserVerificationForm(request.POST)
        user_code = request.POST.get('code')

        if user.code == user_code:
            user.is_active = True
            user.save()
            return redirect(reverse('users:login'))

    else:
        form = UserVerificationForm()

    return render(request, 'users/verification_form.html', {'form': form, 'pk': pk})


def toggle_user_status(request, pk):
    """
    Изменяет статус активности пользователя.
    """
    user = get_object_or_404(User, pk=pk)

    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True

    user.save()

    return redirect('newsletter:view')
