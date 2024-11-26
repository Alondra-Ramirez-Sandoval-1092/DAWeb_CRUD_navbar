from django.shortcuts import render,redirect
from .models import Factura
# Create your views here.

def inicio_vistaFactura(request):
    lafactura=Factura.objects.all()
    return render(request,"gestionarFactura.html",{"mifactura":lafactura})

def registrarFactura(request):
    id_factura=request.POST["skzid_factura"]
    id_paciente=request.POST["skzid_paciente"]
    nombre=request.POST["skznombre"]
    telefono=request.POST["skztel"]
    correo=request.POST["skzcorreo"]
    direccion=request.POST["skzdireccion"]
    servicio=request.POST["skzservicio"]
    costo=request.POST["skzcosto"]

    guardarfactura=Factura.objects.create(id_factura=id_factura,id_paciente=id_paciente,nombre=nombre,
                                                telefono=telefono,correo=correo,direccion=direccion,servicio=servicio,costo=costo)

    return redirect('factura')
    

def seleccionarFactura(request,id_factura):
    factura=Factura.objects.get(id_factura=id_factura)
    return render(request,"editarFactura.html",{"mifactura":factura})

def editarFactura(request):
    id_factura=request.POST["skzid_factura"]
    id_paciente=request.POST["skzid_paciente"]
    nombre=request.POST["skznombre"]
    telefono=request.POST["skztel"]
    correo=request.POST["skzcorreo"]
    direccion=request.POST["skzdireccion"]
    servicio=request.POST["skzservicio"]
    costo=request.POST["skzcosto"]
    factura=Factura.objects.get(id_factura=id_factura)
    factura.id_paciente=id_paciente
    factura.nombre=nombre
    factura.telefono=telefono
    factura.correo=correo
    factura.direccion=direccion
    factura.servicio=servicio
    factura.costo=costo

    factura.save()
    return redirect('factura')
    

def borrarFactura(request,id_factura):
    factura=Factura.objects.get(id_factura=id_factura)
    factura.delete()
    
    return redirect('factura')

