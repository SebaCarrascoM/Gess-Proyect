from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from ...forms import *
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.

@login_required
def agregar_trabajador(request, id_empresa):
    empresa= Empresa.objects.filter(id_empresa= id_empresa)
    data = {
        'empresa':empresa
    }
    result = 0
    if request.method == 'POST':
        #print(request.POST)
        result = 0
        data_trabajador = {
            'id_empresa': id_empresa,
            'nombre_trabajador':request.POST['nombre_trabajador'],
            'rut_trabajador':request.POST['rut_trabajador'],
            'cargo':request.POST['cargo'],
            'area':request.POST['area'],
            'telefono_trabajador':request.POST['telefono_trabajador'],
            'email_trabajador':request.POST['email_trabajador'],
            'fecha_nacimiento':request.POST['fecha_nacimiento'] ,
            'fecha_ingreso':request.POST['fecha_ingreso'],
            'direccion_trabajador':request.POST['direccion_trabajador']             
        }
        formulario_trabajador = TrabajadoresForm(data = data_trabajador)
        if formulario_trabajador.is_valid():
            formulario_trabajador.save() 
            result = 1
            # login(request, user)
        if result == 1:
            messages.success(request, "Solicitud de contacto enviada correctamente.")
            return redirect (to="trabajos")
        else:
            messages.error(request, "error.")

    return render(request, 'app/dashboard/trabajadores/agregar-trabajador.html',data) 

@login_required
def listar_trabajadores(request):
    data = {}
    trabajadores = Trabajadores.objects.all()
    data["entity_trabajadores"]= trabajadores
    
    return render(request, 'app/dashboard/trabajadores/trabajadores.html',data)