from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateView, RegisterView
from django.contrib import admin
from django.urls import path, include

app_name = UsersConfig.name

urlpatterns = [
    # Путь для стандартного LoginView с указанием шаблона для страницы входа
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

    # Путь для выхода из системы
    path('logout/', LogoutView.as_view(), name='logout'),

    # Путь для регистрации
    # path('register/', UserCreateView.as_view, name='register'),
    path('register/', RegisterView.as_view(), name='register'),
]
