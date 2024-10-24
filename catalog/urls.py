from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import products_list, products_detail
from django.urls import path

app_name = CatalogConfig.name

urlpatterns = [
    path('', products_list, name='products_list'),
    path('products/<int:pk>/', products_detail, name='products_detail'),
    path('', views.home, name='home'),
]
