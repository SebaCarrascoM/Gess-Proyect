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
def agregar_gestion(request):
    result = 0
    if request.method == 'POST':
        print(request.POST)
        result=1
        formulario_achs_gestion = AchsGestionForm(data = request.POST)
        if formulario_achs_gestion.is_valid():
            formulario_achs_gestion.save()
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
    return render(request, 'app/dashboard/achs-gestion/agregar-gestion.html',data) 

@login_required
def listar_gestiones(request):
    data = {}
    achs_gestion = AchsGestion.objects.all()
    data["entity_achs_gestion"]= achs_gestion
    
    return render(request, 'app/dashboard/achs-gestion/achs-gestiones.html',data)