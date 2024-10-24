from django.urls import path
from ShoppingList.views import index

urlspatterns = [
    path('', index),
]