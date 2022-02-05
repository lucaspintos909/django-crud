from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def books(request):
    books = Book.objects.all();
    return render(request, 'books/index.html', {"books": books})

def create_book(request):
    form = BookForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('books')

    return render(request, 'books/create.html', {"form": form})

def edit_book(request):
    return render(request, 'books/edit.html')

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('books')
