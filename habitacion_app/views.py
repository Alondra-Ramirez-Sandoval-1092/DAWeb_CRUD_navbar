from django.shortcuts import render,redirect
from .models import Habitacion
# Create your views here.

def inicio_vistaHabitacion(request):
    lahabitacion=Habitacion.objects.all()
    return render(request,"gestionarHabitacion.html",{"mihabitacion":lahabitacion})

def registrarHabitacion(request):
    id_habitacion=request.POST["skzid_habitacion"]
    id_empleado=request.POST["skzid_empleado"]
    id_paciente=request.POST["skzid_paciente"]
    nombre=request.POST["skznombre"]
    telefono=request.POST["skztel"]
    correo=request.POST["skzcorreo"]
    fecha_at=request.POST["skzfecha_at"]
    costo=request.POST["skzcosto"]

    guardarhabitacion=Habitacion.objects.create(id_habitacion=id_habitacion,id_empleado=id_empleado,id_paciente=id_paciente,nombre=nombre,
                                                telefono=telefono,correo=correo,fecha_at=fecha_at,costo=costo)

    return redirect('habitacion')
    

def seleccionarHabitacion(request,id_habitacion):
    habitacion=Habitacion.objects.get(id_habitacion=id_habitacion)
    return render(request,"editarHabitacion.html",{"mihabitacion":habitacion})

def editarHabitacion(request):
    id_habitacion=request.POST["skzid_habitacion"]
    id_empleado=request.POST["skzid_empleado"]
    id_paciente=request.POST["skzid_paciente"]
    nombre=request.POST["skznombre"]
    telefono=request.POST["skztel"]
    correo=request.POST["skzcorreo"]
    fecha_at=request.POST["skzfecha_at"]
    costo=request.POST["skzcosto"]
    habitacion=Habitacion.objects.get(id_habitacion=id_habitacion)
    habitacion.id_empleado=id_empleado
    habitacion.id_paciente=id_paciente
    habitacion.nombre=nombre
    habitacion.telefono=telefono
    habitacion.correo=correo
    habitacion.fecha_at=fecha_at
    habitacion.costo=costo

    habitacion.save()
    return redirect('habitacion')
    

def borrarHabitacion(request,id_habitacion):
    habitacion=Habitacion.objects.get(id_habitacion=id_habitacion)
    habitacion.delete()
    
    return redirect('habitacion')

