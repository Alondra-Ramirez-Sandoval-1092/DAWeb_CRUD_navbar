from django.db import models

# Create your models here.
class Paciente(models.Model):
    id_paciente=models.CharField(primary_key=True,max_length=6)
    id_empleado=models.CharField(max_length=6)
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    correo=models.CharField(max_length=40)
    direccion=models.CharField(max_length=80)
    tiposangre=models.CharField(max_length=12)

    def __str__(self) :
        return self.nombre