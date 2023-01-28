from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from ...forms import *
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.http import Http404
#from pydrive.auth import GoogleAuth

#gauth = GoogleAuth()
#gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
# Create your views here.

@login_required
def agregar_archivo_trabajador(request,id_empresa):
    empresa= Empresa.objects.filter(id_empresa=id_empresa)
    data= {
        'empresa':empresa
    }
    if request.method == 'POST':
        result = 0
        data_archivo = {
            'id_empresa' : id_empresa,
            'tipo_documento' : request.POST['tipo_documento'],
            'documento_empresa': request.FILES['documento_empresa'],  
            'fecha_expedicion':request.POST['fecha_expedicion'],
            'fecha_vencimiento':request.POST['fecha_vencimiento'], 
            'observaciones':request.POST['observaciones'] 
        }  
        print(data_archivo)
        formulario_archivo = ArchivoEmpresaForm(data = data_archivo, files=request.FILES)
        
        if formulario_archivo.is_valid():  
            formulario_archivo.save() 
            result = 1
        # login(request, user)
        if result == 1:
            messages.success(request, "Solicitud de contacto enviada correctamente.")
            return redirect (to="archivos")
        else:
            messages.error(request, "error.")   

    return render(request, 'app/dashboard/archivo-empresa/agregar-archivo.html',data) 


@login_required
def listar_archivos_trabajador(request):
    data = {}
    archivos = ArchivoTrabajadores.objects.all()
    data["entity_archivo"]= archivos
    
    return render(request, 'app/dashboard/archivo-empresa/archivos.html',data)