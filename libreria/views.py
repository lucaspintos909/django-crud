from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def books(request):
    books = Book.objects.all();
    return render(request, 'books/index.html', {"books": books})

def create_book(request):
    return render(request, 'books/create.html')

def edit_book(request):
    return render(request, 'books/edit.html')