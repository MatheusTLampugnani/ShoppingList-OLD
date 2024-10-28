from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db import connection
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        senha = request.POST['senha']

        if nome is not None:
            login(request, nome)
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha incorretos')

    return render(request, 'login.html')


def registro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        confirmar_senha = request.POST['confirmar_senha']

        if senha != confirmar_senha:
            messages.error(request, "As senhas não correspondem.")
            return redirect('registro')

        user = User.objects.create(
            username=nome,
            email=email,
            password=senha
        )
        messages.success(request, "Usuário registrado com sucesso!")
        return redirect('login')
    
    return render(request, 'registro.html')