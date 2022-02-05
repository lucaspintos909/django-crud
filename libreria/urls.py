from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('libros', views.books, name="books"),
    path('libros/ingresar', views.create_book, name="create_book"),
    path('libros/editar', views.edit_book, name="edit_book"),
]
