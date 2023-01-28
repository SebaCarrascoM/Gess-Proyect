from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from ...forms import *
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.http import Http404
from googleapiclient.http import MediaFileUpload
from django.dispatch import receiver
from django.conf import settings
from .GoogleDrive import Create_Service
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
import os
import io
import time
from ...models import ArchivoEmpresa
import pandas as pd



CLIENT_SECRET_FILE = "client_secrets.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = "1d2JtpvcHJCevxXUcSsyI9b__FP0P0A7b"



@login_required
def agregar_archivo_empresa(request,id_empresa):
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
        archivo_nombre = ArchivoEmpresa(documento_empresa=request.FILES['documento_empresa'],
            fecha_vencimiento=request.POST['fecha_vencimiento'],
            observaciones= request.POST['observaciones'],
            fecha_expedicion=request.POST['fecha_expedicion'],
            id_empresa_id=id_empresa,
            tipo_documento=request.POST['tipo_documento']
            )
        archivo_nombre.save()
        file_names = archivo_nombre
        mime_types = "application/pdf"
        file_metadata = {
            'name': str(file_names),
            'parents': [folder_id]
        }
        media = MediaFileUpload(os.getcwd()+"\\media\\"+str(file_names), mimetype=mime_types)
        file=service.files().create(
        body=file_metadata,
        media_body = media,
        fields = "id"
        ).execute()

        formulario_archivo = ArchivoEmpresaForm(data = data_archivo, files=request.FILES)
        if formulario_archivo.is_valid():  
            
            
            id=archivo_nombre.id_documento_empresa
            print(id)
            archivo_creado = ArchivoEmpresa.objects.filter(id_documento_empresa=id)
            archivo_creado.delete()   
            
            
            link ="https://drive.google.com/file/d/"+file['id']+"/view"
            archivo_update = ArchivoEmpresa(documento_empresa=link,
            fecha_vencimiento=request.POST['fecha_vencimiento'],
            observaciones= request.POST['observaciones'],
            fecha_expedicion=request.POST['fecha_expedicion'],
            id_empresa_id=id_empresa,
            tipo_documento=request.POST['tipo_documento'])
            archivo_update.save()
            result = 1 
            
        # login(request, user)
        if result == 1:
                
            
            messages.success(request, "Solicitud de contacto enviada correctamente.")
            return redirect (to="archivos")
            
        else:
            messages.error(request, "error.")
        
    return render(request, 'app/dashboard/archivo-empresa/agregar-archivo.html',data) 

@login_required
def listar_archivos(request):
    data = {}
    archivos = ArchivoEmpresa.objects.all()
    data["entity_archivo"]= archivos
    return render(request, 'app/dashboard/archivo-empresa/archivos.html',data)
    
