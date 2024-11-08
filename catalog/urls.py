from django.urls import path
from catalog.apps import CatalogConfig
from .views import ProductDeleteView, ProductUpdateView, ProductCreateView, ProductDetailView, ProductListView, \
    ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    # Главная страница - список продуктов
    path('', ProductListView.as_view(), name='home'),

    # Страница создания нового продукта
    path('product/new/', ProductCreateView.as_view(), name='product_create'),

    # Страница детальной информации о продукте
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

    # Страница редактирования продукта
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),

    # Страница удаления продукта
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    # Страница контактов
    path('contacts/', ContactsView.as_view(), name='contacts'),
]
