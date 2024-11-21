from django.core.cache import cache
from .models import Product


def get_products_by_category(category_id):
    return Product.objects.filter(category_id=category_id)


def get_products_by_category(category_id):
    cache_key = f'products_in_category_{category_id}'
    products = cache.get(cache_key)

    if not products:
        products = Product.objects.filter(category_id=category_id).values('id', 'name', 'price')
        cache.set(cache_key, list(products), timeout=60 * 15)  # Кеш на 15 минут

    return products
