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
def agregar_trabajador(request):
    result = 0
    if request.method == 'POST':
        print(request.POST)
        result=1
        formulario_trabajador = TrabajadoresForm(data = request.POST)
        if formulario_trabajador.is_valid():
            formulario_trabajador.save()
        else:
            result = 0
        if result == 1:
            messages.success(request, "Solicitud de contacto enviada correctamente.")
            return redirect (to="trabajadores")
        else:
            messages.error(request, "error.")

    data = {}
    empresas = Empresa.objects.all()
    data["entity_empresa"]= empresas
    return render(request, 'app/dashboard/trabajadores/agregar-trabajador.html',data) 

@login_required
def listar_trabajadores(request):
    data = {}
    trabajadores = Trabajadores.objects.all()
    data["entity_trabajadores"]= trabajadores
    
    return render(request, 'app/dashboard/trabajadores/trabajadores.html',data)