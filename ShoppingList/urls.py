from django.urls import path
from ShoppingList.views import index, criarlista, login, registro

urlpatterns = [
    path('', index, name='index'),
    path('criarlista/', criarlista, name='criarlista'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
]