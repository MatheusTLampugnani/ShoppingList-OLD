from django.shortcuts import render, redirect

def index(request):
    return render(request, 'templates/index.html')

def criarlista(request):
    return render(request, 'templates/criarlista.html')