from django.contrib import messages
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, FormView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin  # Импортируем миксин
from django.http import HttpResponseForbidden
from catalog.forms.forms import ContactForm, ProductForm
from catalog.models import Product


class ProductListView(ListView):
    """
    Представление главной страницы
    """
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Устанавливаем владельца
        return super().form_valid(form)


class ProductDetailView(DetailView):
    """
    Представление страницы товара
    """
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner != request.user:
            return HttpResponseForbidden("Вы не можете редактировать этот продукт.")
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner != request.user and not request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponseForbidden("Вы не можете удалить этот продукт.")
        return super().dispatch(request, *args, **kwargs)


class ContactsView(FormView):
    """
    Представление страницы контактов
    """
    template_name = "catalog/contacts.html"
    form_class = ContactForm
    success_url = reverse_lazy("catalog:contacts")

    def form_valid(self, form):
        """
        Переопределение метода для отправки письма при успешной отправки формы
        """
        name = form.cleaned_data["name"]
        message = form.cleaned_data["message"]
        subject = f"Новое сообщение от {name}"
        recipient_list = ["lacryk@gmail.com"]

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email="lacry@rambler.ru",
            to=recipient_list,
        )

        email.headers = {
            "Reply-To": "lacry@rambler.ru",
        }

        email.send(fail_silently=False)

        messages.success(
            self.request, f'Спасибо, {name}! Ваше сообщение "{message}" получено.'
        )  # Добавляем сообщение об успехе
        return super().form_valid(form)  # Вызовем метод родителя для перенаправления на success_url

    def form_invalid(self, form):
        """
        Если форма недействительна, просто отобразим шаблон с ошибками
        """
        return super().form_invalid(form)
