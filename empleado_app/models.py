from django.db import models

# Create your models here.
class Empleado(models.Model):
    id_empleado=models.CharField(primary_key=True,max_length=6)
    id_especialidad=models.CharField(max_length=6)
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    correo=models.CharField(max_length=40)
    puesto=models.CharField(max_length=35)
    horario=models.CharField(max_length=12)
    salario=models.DecimalField(max_digits=12,decimal_places=2)

    def __str__(self) :
        return self.nombre