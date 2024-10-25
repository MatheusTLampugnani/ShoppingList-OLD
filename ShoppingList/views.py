from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db import connection

def index(request):
    return render(request, 'index.html')

def criarlista(request):
    return render(request, 'criarlista.html')

def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, name=name, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha incorretos')

    return render(request, 'login.html')

def registro(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('registro')

        try:
            user = User.objects.create_user(name=name, password=password)
            user.save()
            messages.success(request, 'Conta criada com sucesso!')
            login(request, user)  # Realiza o login automático após o registro
            return redirect('index')  # Redireciona para a página principal
        except:
            messages.error(request, 'Erro ao criar a conta. Tente um nome de usuário diferente.')
    return render(request, 'registro.html')

def index(request):
    # Realiza a consulta SQL
    with connection.cursor() as cursor:
        cursor.execute("SELECT lc.nome_lista, COUNT(il.id_itens) AS quantidade_itens FROM lista_compra lc LEFT JOIN itens_lista il ON lc.id_lista = il.id_lista GROUP BY lc.nome_lista;") 
        columns = [col[0] for col in cursor.description]
        dados = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    # Passa os dados como contexto para o template
    return render(request, 'index.html', {'dados': dados})