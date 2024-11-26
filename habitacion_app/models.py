from django.db import models

# Create your models here.
class Habitacion(models.Model):
    id_habitacion=models.CharField(primary_key=True,max_length=6)
    id_empleado=models.CharField(max_length=6)
    id_paciente=models.CharField(max_length=6)
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    correo=models.CharField(max_length=30)
    fecha_at=models.DateField()
    costo=models.DecimalField(max_digits=7,decimal_places=2)

    def __str__(self) :
        return self.nombre