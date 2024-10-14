from django.contrib import admin
from .models import Category, Product
from .models import Contact


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")  # Отображаем id и name
    search_fields = ("name",)  # Поиск по name


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",
        "category",
    )  # Отображаем id, name, price и category
    list_filter = ("category",)  # Фильтрация по category
    search_fields = ("name", "description")  # Поиск по name и description


# Регистрация моделей в админке
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.register(Contact)
