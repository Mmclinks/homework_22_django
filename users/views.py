from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms.forms import UserRegistrationForm
from users.models import User
from django.shortcuts import render, redirect
from django.views import View
from .forms.forms import UserRegistrationForm


class UserCreateView(CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('user:login')


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Форма валидна, сохраняем пользователя
            form.save()
            return redirect('users:login')
        return render(request, 'users/register.html', {'form': form})
