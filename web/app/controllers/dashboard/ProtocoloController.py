from django.shortcuts import render, redirect, get_object_or_404
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
        formulario_protocolo = ProtocoloForm(data = data_protocolo)
        if formulario_protocolo.is_valid():
            formulario_protocolo.save() 
            result = 1
        # login(request, user)
        if result == 1:
            messages.success(request, "Solicitud de Protocolo enviada correctamente.")
            return redirect (to="protocolo")
        else:
            messages.error(request, "error.")   

    return render(request, 'app/dashboard/protocolo/agregar-protocolo.html',data) 

@login_required
def listar_protocolo(request):
    data = {}
    protocolo = Protocolo.objects.all()
    data["entity_protocolo"]= protocolo
    
    return render(request, 'app/dashboard/protocolo/protocolos.html',data)

@login_required
def protocolo_edit(request, id_protocolo):
    protocolo_intancia = get_object_or_404(Protocolo, id_protocolo=id_protocolo)
    protocolo = Protocolo.objects.filter(id_protocolo = id_protocolo)
    
    for p in protocolo:
        print(p.id_empresa)
        empresa= Empresa.objects.filter(razon_social= p.id_empresa)
        for emp in empresa:
            id_empresa = emp.id_empresa    
    result = 0
    if request.method == 'POST':
        data_protocolo = {
            'id_empresa': id_empresa,
            'nombre_protocolo':request.POST['nombre_protocolo'],  
            'requisito':request.POST['requisito'],
            'evidencia':request.POST['evidencia'],
            'fecha_realizacion':request.POST['fecha_realizacion'], 
            'proxima_aplicacion':request.POST['proxima_aplicacion']     
        }
        result=1
        formulario_protocolo= ProtocoloForm(data = data_protocolo , instance=protocolo_intancia)
        if formulario_protocolo.is_valid():
            formulario_protocolo.save()
        else:
            result = 0
        if result == 1:
            messages.success(request, "Solicitud de Protocolo enviada correctamente.")
            return redirect (to="protocolo")
        else:
            messages.error(request, "error.")
    
    data = {
        'protocolo':protocolo
    }
    return render(request, "app/dashboard/protocolo/editar-protocolo.html",data)

@login_required
def eliminar_protocolo(request,id_protocolo):
    protocolo = get_object_or_404(Protocolo, id_protocolo=id_protocolo)
    protocolo.delete()
    messages.success(request, "Protocolo eliminada correctamente")
    return redirect(to="protocolo")