from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('libros', views.books, name="books"),
]
