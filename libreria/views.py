from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  return HttpResponse("<h1>Bienvenido a la libreria</h1>")

def nosotros(request):
  return render(request, 'pages/nosotros.html')