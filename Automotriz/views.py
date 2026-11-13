from django.http import HttpResponse

def inicio1(request):
    return HttpResponse("Bienvenido a nuestra tienda automotriz")

def inicio2(request):
    return HttpResponse("Conoce nuestros automoviles")

def inicio3(request):
    return HttpResponse("Conoce a nuestro provedores")

def inicio4(request):
    return HttpResponse("Conoce nuestros presupuestos")

def inicio5(request):
    return HttpResponse("Conoce nuestras ofertas semanales")

from django.shortcuts import render

def bienvenida(request):
    return render(request, 'automotriz/bienvenida.html')

def autos(request):
    return render(request, 'automotriz/autos.html')

def proveedores(request):
    return render(request, 'automotriz/proveedores.html')

def presupuesto(request):
    return render(request, 'automotriz/presupuesto.html')

def oferta(request):
    return render(request, 'automotriz/oferta.html')