from django.shortcuts import render,redirect
from .models import Paciente
# Create your views here.

def inicio_vistaPaciente(request):
    elpaciente=Paciente.objects.all()
    return render(request,"gestionarPaciente.html",{"mipaciente":elpaciente})

def registrarPaciente(request):
    id_paciente=request.POST["skzid_paciente"]
    id_empleado=request.POST["skzid_empleado"]
    nombre=request.POST["skznombre"]
    telefono=request.POST["skztel"]
    correo=request.POST["skzcorreo"]
    direccion=request.POST["skzdireccion"]
    tiposangre=request.POST["skztiposangre"]

    guardarpaciente=Paciente.objects.create(id_paciente=id_paciente,id_empleado=id_empleado,nombre=nombre,telefono=telefono,correo=correo,direccion=direccion,tiposangre=tiposangre)

    return redirect('paciente')
    

def seleccionarPaciente(request,id_paciente):
    paciente=Paciente.objects.get(id_paciente=id_paciente)
    return render(request,"editarPaciente.html",{"mipaciente":paciente})

def editarPaciente(request):
    id_paciente=request.POST["skzid_paciente"]
    id_empleado=request.POST["skzid_empleado"]
    nombre=request.POST["skznombre"]
    telefono=request.POST["skztel"]
    correo=request.POST["skzcorreo"]
    direccion=request.POST["skzdireccion"]
    tiposangre=request.POST["skztiposangre"]
    paciente=Paciente.objects.get(id_paciente=id_paciente)
    paciente.id_empleado=id_empleado
    paciente.nombre=nombre
    paciente.telefono=telefono
    paciente.correo=correo
    paciente.direccion=direccion
    paciente.tiposangre=tiposangre

    paciente.save()
    return redirect('paciente')
    

def borrarPaciente(request,id_paciente):
    paciente=Paciente.objects.get(id_paciente=id_paciente)
    paciente.delete()
    
    return redirect('paciente')

