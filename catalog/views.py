import messages
from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Здесь вы можете добавить код для обработки данных (например, сохранить в БД или отправить по email)

        # Отправляем сообщение об успешной отправке
        messages.success(request, 'Ваше сообщение успешно отправлено!')

        # Перенаправляем обратно на страницу контактов
        return redirect('catalog:contacts')

    return render(request, 'contacts.html')
