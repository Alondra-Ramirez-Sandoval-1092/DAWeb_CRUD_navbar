# Generated by Django 5.1.1 on 2024-11-21 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_paciente', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('id_empleado', models.CharField(max_length=6)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=80)),
                ('tiposangre', models.CharField(max_length=12)),
            ],
        ),
        migrations.DeleteModel(
            name='Empleado',
        ),
    ]