from django.urls import path
from Usuarios.views import login, registro

urlpatterns = [
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
]