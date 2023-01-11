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
def vista_trabajadores(request, id_empresa):
    trabajadores = Trabajadores.objects.filter(id_empresa = id_empresa)

    data = {
        'trabajadores':trabajadores
    }

    return render(request, 'app/dashboard/trabajos/listado-trabajadores.html', data)

@login_required
def agregar_trabajos(request, id_trabajador):
    trabajador = Trabajadores.objects.filter(id_trabajador = id_trabajador)

    for trabajadore in trabajador:
        print(trabajadore.id_empresa)
    data = {
        'trabajador':trabajador
    }
    if request.method == 'POST':
        print(request.POST)
        formulario = TrabajosNuevosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            print(formulario)
            # login(request, user)
            messages.success(request, "Trabajo Creado Exitosamente")
            return redirect(to="trabajos")

    return render(request, 'app/dashboard/trabajos/agregar-trabajos.html', data) 

@login_required
def listar_empresas(request):
    data = {}
    empresa = Empresa.objects.all()
    data["entity_empresa"]= empresa
    
    return render(request, 'app/dashboard/trabajos/empresa.html',data)