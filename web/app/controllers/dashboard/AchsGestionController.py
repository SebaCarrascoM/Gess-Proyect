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
def agregar_gestion(request,id_empresa):
    empresa= Empresa.objects.filter(id_empresa=id_empresa)
    data= {
        'empresa':empresa
    }
    if request.method == 'POST':
        result = 0
        data_gestion = {
            'id_empresa': id_empresa,
            'tipo_requisito':request.POST['tipo_requisito'],  
            'accion':request.POST['accion'],
            'fecha_vencimiento':request.POST['fecha_vencimiento'],
            'observaciones':request.POST['observaciones']           
        }
        formulario_gestion = AchsGestionForm(data = data_gestion)
        if formulario_gestion.is_valid():
            formulario_gestion.save() 
            result = 1
        # login(request, user)
        if result == 1:
            messages.success(request, "Solicitud de contacto enviada correctamente.")
            return redirect (to="trabajos")
        else:
            messages.error(request, "error.")   

    return render(request, 'app/dashboard/achs-gestion/agregar-gestion.html',data) 

@login_required
def listar_gestiones(request):
    data = {}
    achs_gestion = AchsGestion.objects.all()
    data["entity_achs_gestion"]= achs_gestion
    
    return render(request, 'app/dashboard/achs-gestion/achs-gestiones.html',data)