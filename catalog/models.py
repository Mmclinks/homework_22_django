from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        upload_to="images/products/", blank=True, null=True, verbose_name="Изображение"
    )
    category = models.ForeignKey("catalog.Category", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(
        default=False, verbose_name="Опубликован", help_text="Статус публикации продукта"
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="products", verbose_name="Владелец"
    )

    def __str__(self):
        return f"{self.name}. Категория: {self.category}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "category", "price"]
        permissions = [
            ("can_unpublish_product", "Может отменять публикацию продукта"),
        ]
