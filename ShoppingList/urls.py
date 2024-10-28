from django.urls import path
from ShoppingList.views import index, criarlista

urlpatterns = [
    path('', index, name='index'),
    path('criarlista/', criarlista, name='criarlista'),
]