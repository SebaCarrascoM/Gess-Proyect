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
def agregar_protocolo(request):
    result = 0
    if request.method == 'POST':
        print(request.POST)
        result=1
        formulario_protocolo = ProtocoloForm(data = request.POST)
        if formulario_protocolo.is_valid():
            formulario_protocolo.save()
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
    return render(request, 'app/dashboard/protocolo/agregar-protocolo.html',data) 

@login_required
def listar_protocolo(request):
    protocolo = Protocolo.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(protocolo, 5)
        protocolo = paginator.page(page)
    except:
        raise Http404
    
    data = {
        'entity': protocolo,
        'paginator': paginator
    }
    
    return render(request, 'app/dashboard/protocolo/protocolos.html',data)