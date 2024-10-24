from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def criarlista(request):
    return render(request, 'criarlista.html')