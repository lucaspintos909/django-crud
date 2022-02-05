from typing import Any
from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name="Título")
    description = models.TextField(null=True, verbose_name="Descripción")
    image = models.ImageField(upload_to="images/", verbose_name="Imagen", null=True)

    def delete(self, using = None, keep_parents = False):
        self.image.storage.delete(self.image.name)
        super().delete()

    def __str__(self):
        row = f'Libro: {self.title}'
        return row