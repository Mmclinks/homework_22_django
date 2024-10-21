# import messages
# from catalog.models import Product
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import Contact
#
#
# def home(request):
#     latest_products = Product.objects.all()
#     return render(request, "home.html", {"latest_products": latest_products})
#
#
# def contacts(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#
#         # Сохранение данных в базе данных
#         contact = Contact(name=name, phone=phone, message=message)
#         contact.save()
#
#         # Отправляем сообщение об успешной отправке
#         messages.success(request, "Ваше сообщение успешно отправлено!")
#
#         # Перенаправляем обратно на страницу контактов
#         return redirect("catalog:contacts")
#
#     # Извлечение всех контактов для отображения
#     contacts = Contact.objects.all()
#
#     return render(request, "contacts.html", {"contacts": contacts})
#
#
#
from gc import get_objects

from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "product_list.html", context)


def products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'products_detail.html', context)
