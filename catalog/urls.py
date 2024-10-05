from django.urls import path, include
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig

urlpatterns = [
    path('', include('catalog.urls', namespace='catalog')),
    path('', views.home, name='home'),
    path('contacts.html/', views.contacts, name='contacts.html'),
]