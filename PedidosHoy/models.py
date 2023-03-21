from django.db import models
from django.contrib.auth.models import User

class Platillo(models.Model):
    nombre = models.CharField(max_length=100)
    detalle = models.TextField(max_length=1000)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="menues", null=True, blank=True)
    propietario = models.ForeignKey(to=User, on_delete=models.CASCADE , related_name="propietario")

    @property
    def image_url(self):
        return self.imagen.url if self.imagen else ''
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.propietario.id}"

