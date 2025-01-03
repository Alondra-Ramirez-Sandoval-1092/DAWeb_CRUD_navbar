# Generated by Django 5.1.1 on 2024-11-22 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id_habitacion', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('id_empleado', models.CharField(max_length=6)),
                ('id_paciente', models.CharField(max_length=6)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=30)),
                ('fecha_at', models.DateField()),
                ('costo', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
