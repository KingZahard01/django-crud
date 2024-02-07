from django.db import models

# Create your models here.

class Nota(models.Model):
    # nombre del campo = tipo de dato
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # que muestre en admin el nombre y la descripcion de la nota
    def __str__(self):
        return f'Titulo: { self.titulo } - Descripcion: { self.descripcion }'