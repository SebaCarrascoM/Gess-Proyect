from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from ...forms import *
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
import pandas as pd
from django.http import Http404
# Create your views here.

@login_required
def agregar_contacto(request):
    if request.method == 'POST':
        print(request.POST)
        

    return render(request, 'app/dashboard/contacto/agregar-contacto.html') 
@login_required
def listar_contactos(request):
    data = {}
    contacto_empresa = ContactoEmpresa.objects.all()
    empresas = Empresa.objects.all()
    data["entity_empresa"]= empresas
    data["entity_contacto"]= contacto_empresa
    empresa = request.GET.get('empresa')
    data_empresa = empresa
    print(data_empresa)
    return render(request, 'app/dashboard/contacto/contactos.html',data)