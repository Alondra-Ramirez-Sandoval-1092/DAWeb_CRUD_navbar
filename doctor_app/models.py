from django.db import models

# Create your models here.
class Doctor(models.Model):
    id_doctor=models.CharField(primary_key=True,max_length=6)
    id_especialidad=models.CharField(max_length=6)
    id_consultorio=models.CharField(max_length=6)
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    correo=models.CharField(max_length=40)
    horario=models.CharField(max_length=12)

    def __str__(self) :
        return self.nombre