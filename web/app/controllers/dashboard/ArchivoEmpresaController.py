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
import pathlib
from os import remove
import io
import time
from ...models import ArchivoEmpresa
import pandas as pd
from datetime import date



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
            'observaciones':request.POST['observaciones'],
            'dias_restantes' : 0 
        }
        print(data_archivo)

        formulario_archivo = ArchivoEmpresaForm(data = data_archivo, files=request.FILES)
        if formulario_archivo.is_valid():  
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
            
            id=archivo_nombre.id_documento_empresa
            print("media/"+str(archivo_nombre.documento_empresa))
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
    count=0  
    ejemplo_dir = 'media/documentos_empresa/'
    directorio = pathlib.Path(ejemplo_dir)
    for fichero in directorio.iterdir():
        print(fichero.name)
        remove("media/documentos_empresa/"+fichero.name)
    
    data = {}
    archivos = ArchivoEmpresa.objects.all()
    for ar in archivos:
        if ar.fecha_vencimiento >= date.today():
            dias_a_vencer=ar.fecha_vencimiento-date.today()
            ArchivoEmpresa.objects.filter(id_documento_empresa=ar.id_documento_empresa).update(dias_restantes=str(dias_a_vencer.days))
        else:
            dias_vencidos = date.today()-ar.fecha_vencimiento
            ArchivoEmpresa.objects.filter(id_documento_empresa=ar.id_documento_empresa).update(dias_restantes=str(dias_vencidos.days))
            count+=1
            messages.warning(request,"archivos vencidos "+ str(count) )
    data["entity_archivo"]= archivos
    fecha_hoy=date.today()
    data["fecha_hoy"]=fecha_hoy
    
    

    return render(request, 'app/dashboard/archivo-empresa/archivos.html',data)