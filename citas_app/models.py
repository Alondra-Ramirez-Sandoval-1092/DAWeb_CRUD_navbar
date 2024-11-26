from django.db import models

# Create your models here.
class Citas(models.Model):
    id_cita=models.CharField(primary_key=True,max_length=6)
    id_empleado=models.CharField(max_length=6)
    id_paciente=models.CharField(max_length=6)
    nombre=models.CharField(max_length=100)
    fecha_reg=models.DateTimeField(auto_now_add=True)
    fecha_at=models.DateField()
    descripcion=models.CharField(max_length=150)
    costo=models.DecimalField(max_digits=7,decimal_places=2)

    def __str__(self) :
        return self.nombre