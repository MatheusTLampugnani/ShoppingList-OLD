from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')

def criarlista(request):
    return render(request, 'criarlista.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha incorretos')

    return render(request, 'login.html')

def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('registro')

        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Conta criada com sucesso!')
            login(request, user)  # Realiza o login automático após o registro
            return redirect('home')  # Redireciona para a página principal
        except:
            messages.error(request, 'Erro ao criar a conta. Tente um nome de usuário diferente.')
    
    return render(request, 'registro.html')

