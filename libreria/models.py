from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Libro(models.Model):
    ESTADOS = [
        ('PR', 'Por leer'),
        ('LE', 'Leyendo'),
        ('LD', 'Leído'),
    ]

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=2, choices=ESTADOS)
    resena_personal = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo
