from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('libros', views.books, name="books"),
    path('libros/ingresar', views.create_book, name="create_book"),
    path('libros/editar', views.edit_book, name="edit_book"),
    path('libros/delete/<int:id>', views.delete_book, name="delete_book"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
