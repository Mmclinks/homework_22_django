from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig

from .views import (ContactsView, ProductCreateView, ProductDeleteView,
                    ProductDetailView, ProductListView, ProductUpdateView)
from .views import ProductsByCategoryView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("product/new/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path(
        "product/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("", views.ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("product/create/", views.ProductCreateView.as_view(), name="product_create"),
    path(
        "product/<int:pk>/update/",
        views.ProductUpdateView.as_view(),
        name="product_update",
    ),
    path(
        "product/<int:pk>/delete/",
        views.ProductDeleteView.as_view(),
        name="product_delete",
    ),
    path("", ProductListView.as_view(), name="products_list"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path('category/<int:category_id>/', ProductsByCategoryView.as_view(), name='products_by_category'),
]
