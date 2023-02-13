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
def listar_oa(request):
    data = {}
    oa = Oa.objects.all()
    data["entity_oa"]= oa
    
    return render(request, 'app/dashboard/oa/oa.html',data)

@login_required
def oa_edit(request, id_oa):
    oa_intancia = get_object_or_404(Oa, id_oa=id_oa)
    oa = Oa.objects.filter(id_oa = id_oa)
    
    for o in oa:
        print(o.id_empresa)
        empresa= Empresa.objects.filter(razon_social= o.id_empresa)
        for emp in empresa:
            id_empresa = emp.id_empresa    
    result = 0
    if request.method == 'POST':
        print(request.POST)
        data_oa = {
            'usuario_web':request.POST['usuario_web'],
            'clave_web':request.POST['clave_web'],
            'asesor_oa':request.POST['asesor_oa'],
            'telefono':request.POST['telefono'],
            'correo_oa':request.POST['correo_oa'],
            'id_empresa':id_empresa
        }
        result=1
        formulario_oa= OaForm(data = data_oa , instance=oa_intancia)
        if formulario_oa.is_valid():
            
            formulario_oa.save()
        else:
            result = 0
        if result == 1:
            messages.success(request, "Solicitud de contacto enviada correctamente.")
            return redirect (to="oa")
        else:
            messages.error(request, "error.")
    
    data = {
        'oa':oa
    }
    return render(request, "app/dashboard/oa/editar-oa.html",data)