# Generated by Django 5.1.1 on 2024-11-21 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('id_especialidad', models.CharField(max_length=6)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=40)),
                ('puesto', models.CharField(max_length=35)),
                ('horario', models.CharField(max_length=12)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]