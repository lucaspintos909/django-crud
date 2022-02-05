from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def books(request):
    return render(request, 'books/index.html')

def create_book(request):
    return render(request, 'books/create.html')

def edit_book(request):
    return render(request, 'books/edit.html')