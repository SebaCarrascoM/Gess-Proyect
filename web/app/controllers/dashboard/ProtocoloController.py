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
def agregar_protocolo(request,id_empresa):
    empresa= Empresa.objects.filter(id_empresa=id_empresa)
    data= {
        'empresa':empresa
    }
    if request.method == 'POST':
        result = 0
        data_protocolo = {
            'id_empresa': id_empresa,
            'nombre_protocolo':request.POST['nombre_protocolo'],  
            'requisito':request.POST['requisito'],
            'evidencia':request.POST['evidencia'],
            'fecha_realizacion':request.POST['fecha_realizacion'], 
            'proxima_aplicacion':request.POST['proxima_aplicacion']     
        }
        formulario_protocolo = AchsGestionForm(data = data_protocolo)
        if formulario_protocolo.is_valid():
            formulario_protocolo.save() 
            result = 1
        # login(request, user)
        if result == 1:
            messages.success(request, "Solicitud de contacto enviada correctamente.")
            return redirect (to="trabajos")
        else:
            messages.error(request, "error.")   

    return render(request, 'app/dashboard/achs-gestion/agregar-gestion.html',data) 

@login_required
def listar_protocolo(request):
    data = {}
    protocolo = Protocolo.objects.all()
    data["entity_protocolo"]= protocolo
    
    return render(request, 'app/dashboard/protocolo/protocolos.html',data)