from django.urls import path
from . import views

urlpatterns = [
    path('inicio1/', views.inicio1),
    path('inicio2/', views.inicio2),
    path('inicio3/', views.inicio3),
    path('inicio4/', views.inicio4),
    path('inicio5/', views.inicio5),
    path('bienvenida/', views.bienvenida),
    path('autos/', views.autos),
    path('proveedores/', views.proveedores),
    path('presupuesto/', views.presupuesto),
    path('oferta/', views.oferta),
]

