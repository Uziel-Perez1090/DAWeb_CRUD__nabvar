from django.shortcuts import render,redirect
from.models import Proveedor
# Create your views here.

def inicio_vista(request):
    losproveedores=Proveedor.objects.all()

    return render(request,"gestionarProveedor.html",{"misproveedores":losproveedores})


def registrarProveedor(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["txttelefono"]
    email=request.POST["txtemail"]
    cantidad=request.POST["txtcantidad"]
    direccion=request.POST["txtdireccion"]
    horario=request.POST["txthorario"]
    guardarproveedor=Proveedor.objects.create(codigo=codigo,nombre=nombre,telefono=telefono,email=email,cantidad=cantidad,direccion=direccion,horario=horario)
    return redirect("Proveedores")

def seleccionarProveedor(request,codigo):
    negocio=Proveedor.objects.get(codigo=codigo)
    return render(request,"editarProveedor.html",{"misproveedores":negocio})

def editarProveedor(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["txttelefono"]
    email=request.POST["txtemail"]
    cantidad=request.POST["txtcantidad"]
    direccion=request.POST["txtdireccion"]
    horario=request.POST["txthorario"]
    negocio=Proveedor.objects.get(codigo=codigo)
    negocio.nombre=nombre
    negocio.telefono=telefono
    negocio.email=email
    negocio.cantidad=cantidad
    negocio.direccion=direccion
    negocio.horario=horario
    negocio.save()
    return redirect("Proveedores")

def borrarProveedor(request,codigo):
    materia=Proveedor.objects.get(codigo=codigo)
    materia.delete()
    return redirect("Proveedores")