from django.shortcuts import render,redirect
from .models import Empleado
# Create your views here.

def inicio_vistaEmpleado(request):
    elempleado=Empleado.objects.all()
    return render(request,"gestionarEmpleado.html",{"miempleado":elempleado})

def registrarEmpleado(request):
    id_empleado=request.POST["skzid_empleado"]
    id_especialidad=request.POST["skzid_especialidad"]
    nombre=request.POST["skznombre"]
    telefono=request.POST["skztel"]
    correo=request.POST["skzcorreo"]
    puesto=request.POST["skzpuesto"]
    horario=request.POST["skzhorario"]
    salario=request.POST["skzsalario"]

    guardarempleado=Empleado.objects.create(id_empleado=id_empleado,id_especialidad=id_especialidad,nombre=nombre,telefono=telefono,correo=correo,puesto=puesto,horario=horario,salario=salario)

    return redirect('empleado')
    

def seleccionarEmpleado(request,id_empleado):
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    return render(request,"editarEmpleado.html",{"miempleado":empleado})

def editarEmpleado(request):
    id_empleado=request.POST["skzid_empleado"]
    id_especialidad=request.POST["skzid_especialidad"]
    nombre=request.POST["skznombre"]
    telefono=request.POST["skztel"]
    correo=request.POST["skzcorreo"]
    puesto=request.POST["skzpuesto"]
    horario=request.POST["skzhorario"]
    salario=request.POST["skzsalario"]
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    empleado.id_especialidad=id_especialidad
    empleado.nombre=nombre
    empleado.telefono=telefono
    empleado.correo=correo
    empleado.puesto=puesto
    empleado.horario=horario
    empleado.salario=salario

    empleado.save()
    return redirect('empleado')
    

def borrarEmpleado(request,id_empleado):
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    empleado.delete()
    
    return redirect('empleado')

