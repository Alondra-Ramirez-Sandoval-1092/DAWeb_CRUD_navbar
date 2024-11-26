from django.shortcuts import render,redirect
from .models import Doctor
# Create your views here.

def inicio_vistaDoctor(request):
    eldoctor=Doctor.objects.all()
    return render(request,"gestionarDoctor.html",{"midoctor":eldoctor})

def registrarDoctor(request):
    id_doctor=request.POST["skzid_doctor"]
    id_especialidad=request.POST["skzid_especialidad"]
    id_consultorio=request.POST["skzid_consultorio"]
    nombre=request.POST["skznombre"]
    telefono=request.POST["skztel"]
    correo=request.POST["skzcorreo"]
    horario=request.POST["skzhorario"]

    guardardoctor=Doctor.objects.create(id_doctor=id_doctor,id_especialidad=id_especialidad,id_consultorio=id_consultorio,nombre=nombre,telefono=telefono,correo=correo,horario=horario)

    return redirect('doctor')
    

def seleccionarDoctor(request,id_doctor):
    doctor=Doctor.objects.get(id_doctor=id_doctor)
    return render(request,"editarDoctor.html",{"midoctor":doctor})

def editarDoctor(request):
    id_doctor=request.POST["skzid_doctor"]
    id_especialidad=request.POST["skzid_especialidad"]
    id_consultorio=request.POST["skzid_consultorio"]
    nombre=request.POST["skznombre"]
    telefono=request.POST["skztel"]
    correo=request.POST["skzcorreo"]
    horario=request.POST["skzhorario"]
    doctor=Doctor.objects.get(id_doctor=id_doctor)
    doctor.id_especialidad=id_especialidad
    doctor.id_consultorio=id_consultorio
    doctor.nombre=nombre
    doctor.telefono=telefono
    doctor.correo=correo
    doctor.horario=horario

    doctor.save()
    return redirect('doctor')
    

def borrarDoctor(request,id_doctor):
    doctor=Doctor.objects.get(id_doctor=id_doctor)
    doctor.delete()
    
    return redirect('doctor')

