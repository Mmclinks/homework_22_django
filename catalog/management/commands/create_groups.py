from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = "Создание группы 'Модератор продуктов' с правами"

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name="Модератор продуктов")
        if created:
            self.stdout.write("Группа 'Модератор продуктов' создана.")

        content_type = ContentType.objects.get_for_model(Product)
        unpublish_permission, _ = Permission.objects.get_or_create(
            codename="can_unpublish_product",
            name="Может отменять публикацию продукта",
            content_type=content_type,
        )
        delete_permission = Permission.objects.get(codename="delete_product", content_type=content_type)

        group.permissions.add(unpublish_permission, delete_permission)
        self.stdout.write("Права добавлены группе.")
