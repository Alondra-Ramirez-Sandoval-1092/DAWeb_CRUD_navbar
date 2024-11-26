from django.shortcuts import render,redirect
from .models import Citas
# Create your views here.

def inicio_vistaCita(request):
    lacita=Citas.objects.all()
    return render(request,"gestionarCita.html",{"micita":lacita})

def registrarCita(request):
    id_cita=request.POST["skzid_cita"]
    id_empleado=request.POST["skzid_empleado"]
    id_paciente=request.POST["skzid_paciente"]
    nombre=request.POST["skznombre"]
    # fecha_reg=request.POST["skzfecha_reg"]
    fecha_at=request.POST["skzfecha_at"]
    descripcion=request.POST["skzdescripcion"]
    costo=request.POST["skzcosto"]

    guardarcita=Citas.objects.create(id_cita=id_cita,id_empleado=id_empleado,id_paciente=id_paciente,nombre=nombre,fecha_at=fecha_at,descripcion=descripcion,costo=costo)

    return redirect('cita')
    

def seleccionarCita(request,id_cita):
    cita=Citas.objects.get(id_cita=id_cita)
    return render(request,"editarCita.html",{"micita":cita})

def editarCita(request):
    id_cita=request.POST["skzid_cita"]
    id_empleado=request.POST["skzid_empleado"]
    id_paciente=request.POST["skzid_paciente"]
    nombre=request.POST["skznombre"]
    # fecha_reg=request.POST["skzfecha_reg"]
    fecha_at=request.POST["skzfecha_at"]
    descripcion=request.POST["skzdescripcion"]
    costo=request.POST["skzcosto"]
    cita=Citas.objects.get(id_cita=id_cita)
    cita.id_empleado=id_empleado
    cita.id_paciente=id_paciente
    cita.nombre=nombre
    # cita.fecha_reg=fecha_reg
    cita.fecha_at=fecha_at
    cita.descripcion=descripcion
    cita.costo=costo

    cita.save()
    return redirect('cita')
    

def borrarCita(request,id_cita):
    cita=Citas.objects.get(id_cita=id_cita)
    cita.delete()
    
    return redirect('cita')

