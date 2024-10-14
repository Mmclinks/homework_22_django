from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Добавляет тестовые продукты в базу данных"

    def handle(self, *args, **kwargs):
        # Удаляем все существующие данные из моделей Product и Category
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создаем тестовые категории
        electronics = Category.objects.create(
            name="Электроника", description="Все виды электроники."
        )
        clothing = Category.objects.create(
            name="Одежда", description="Мужская и женская одежда."
        )
        books = Category.objects.create(name="Книги", description="Разные жанры книг.")

        # Создаем тестовые продукты
        Product.objects.create(
            name="Смартфон",
            description="Современный смартфон с большими возможностями.",
            category=electronics,
            price=599.99,
        )
        Product.objects.create(
            name="Футболка",
            description="Удобная футболка из хлопка.",
            category=clothing,
            price=19.99,
        )
        Product.objects.create(
            name="Учебник по программированию",
            description="Учебник для изучения программирования на Python.",
            category=books,
            price=29.99,
        )

        self.stdout.write(self.style.SUCCESS("Тестовые продукты успешно добавлены!"))
