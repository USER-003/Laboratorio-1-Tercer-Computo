from django.shortcuts import render
from .models import Cliente, Venta, Empleado, Area

def home(request):
    return render(request, "index.html")

def cliente(request):
    clientes = Cliente.objects.all()
    return render(request, "cliente.html", {"clientes":clientes})

def venta(request):
    ventas = Venta.objects.all()
    return render(request, "venta.html", {"ventas":ventas})

def empleado(request):
    empleados = Empleado.objects.all()
    return render(request, "empleado.html", {"empleados":empleados})

def area(request):
    areas = Area.objects.all()
    return render(request, "area.html", {"areas":areas})