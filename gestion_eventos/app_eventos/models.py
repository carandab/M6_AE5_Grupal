from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Meta:
        permissions = [
            ("registrar_evento", "Puede ver la sección de ventas"),
            ("registrar_persona", "Puede ver la sección de compras"),
        ]    