from datetime import datetime
from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()

    def anio_nacimiento(self):
        anio_actual = datetime.now().year
        valor = anio_actual - self.edad
        return valor
    
    def obtener_ciudad(self):
        if(self.cedula.startswith("11")):
            return "Loja"
        else:
            return "Otra Ciudad"

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - CI: {self.obtener_ciudad()} - Edad: {self.edad} - Año de Nacimiento: {self.anio_nacimiento()}"
