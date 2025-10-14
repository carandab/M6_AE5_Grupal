from django.db import models
from django.contrib.auth.models import AbstractUser




class CustomUser(AbstractUser):
    class Meta:
        permissions = [
            ("registrar_evento", "Puede ver la sección de ventas"),
            ("registrar_persona", "Puede ver la sección de compras"),
        ]    

class Eventos(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    lugar = models.TextField()
    fecha = models.DateTimeField(help_text="Fecha y Hora")
    imagen = models.ImageField(upload_to='eventos/', null=True, blank=True)

    def __str__(self):
        return self.nombre