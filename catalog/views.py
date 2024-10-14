import messages
from catalog.models import Product
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def home(request):
    # Получаем последние 5 созданных продуктов
    latest_products = Product.objects.order_by("-created_at")[:5]

    # Выводим их в консоль
    for product in latest_products:
        print(
            f"Product ID: {product.id}, Name: {product.name}, Price: {product.price}, Created At: {product.created_at}"
        )

    return render(request, "home.html", {"latest_products": latest_products})


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # Сохранение данных в базе данных
        contact = Contact(name=name, phone=phone, message=message)
        contact.save()

        # Отправляем сообщение об успешной отправке
        messages.success(request, "Ваше сообщение успешно отправлено!")

        # Перенаправляем обратно на страницу контактов
        return redirect("catalog:contacts")

    # Извлечение всех контактов для отображения
    contacts = Contact.objects.all()

    return render(request, "contacts.html", {'contacts': contacts})
