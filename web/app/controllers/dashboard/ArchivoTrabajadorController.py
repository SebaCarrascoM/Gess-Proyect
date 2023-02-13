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

folder_id = "1KfebOArPb6a9nqsplDiLbraxa4mcgBuL"


@login_required
def agregar_archivo_trabajador(request,id_trabajador):
    trabajador = Trabajadores.objects.filter(id_trabajador = id_trabajador)

    for tbj in trabajador:
        empresa= Empresa.objects.filter(razon_social= tbj.id_empresa)
        for emp in empresa:
            id_empresa =emp.id_empresa
            print(id_empresa)
            print(id_trabajador)
    data = {
        'trabajador':trabajador,
        'empresa':empresa
    }
    if request.method == 'POST':
        result = 0
        data_archivo = {
            
            'tipo_archivo' : request.POST['tipo_archivo'],
            'documento_trabajador': request.FILES['documento_trabajador'],  
            'fecha_expedicion':request.POST['fecha_expedicion'],
            'fecha_vencimiento':request.POST['fecha_vencimiento'], 
            'observaciones':request.POST['observaciones'] ,
            'id_empresa' : id_empresa,
            'id_trabajador': id_trabajador,
            'dias_restantes' : 0
        }  
        print(data_archivo)
        formulario_archivo = ArchivoTrabajadorForm(data = data_archivo, files=request.FILES)
        
        if formulario_archivo.is_valid():  
            archivo_nombre = ArchivoTrabajadores(
            documento_trabajador=request.FILES['documento_trabajador'],
            fecha_vencimiento=request.POST['fecha_vencimiento'],
            observaciones= request.POST['observaciones'],
            fecha_expedicion=request.POST['fecha_expedicion'],
            id_empresa_id=id_empresa,
            id_trabajador_id = id_trabajador,
            tipo_archivo=request.POST['tipo_archivo']
            )
            print(archivo_nombre.documento_trabajador)
            archivo_nombre.save()
            file_names = archivo_nombre.documento_trabajador
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
            
            id=archivo_nombre.id_archivo_trabajador

            archivo_creado = ArchivoTrabajadores.objects.filter(id_archivo_trabajador=id)
            archivo_creado.delete()   
            
            link ="https://drive.google.com/file/d/"+file['id']+"/view"
            archivo_update = ArchivoTrabajadores(documento_trabajador=link,
            fecha_vencimiento=request.POST['fecha_vencimiento'],
            observaciones= request.POST['observaciones'],
            fecha_expedicion=request.POST['fecha_expedicion'],
            id_empresa_id=id_empresa,
            id_trabajador_id=id_trabajador,
            tipo_archivo=request.POST['tipo_archivo'])
            archivo_update.save()
            result = 1 
            
        # login(request, user)
        if result == 1:
                
            
            messages.success(request, "Solicitud de contacto enviada correctamente.")
            return redirect (to="archivos-trabajador")
            
        else:
            messages.error(request, "error.")  

    return render(request, 'app/dashboard/archivo-trabajador/agregar-archivo.html',data) 


@login_required
def listar_archivos_trabajador(request):
    ejemplo_dir = 'media/documentos_trabajador/'
    directorio = pathlib.Path(ejemplo_dir)
    for fichero in directorio.iterdir():
        print(fichero.name)
        remove("media/documentos_trabajador/"+fichero.name)
    archivos = ArchivoTrabajadores.objects.all()
    for ar in archivos:
        if ar.fecha_vencimiento >= date.today():
            dias_a_vencer=ar.fecha_vencimiento-date.today()
            ArchivoTrabajadores.objects.filter(id_archivo_trabajador=ar.id_archivo_trabajador).update(dias_restantes=str(dias_a_vencer.days))
        else:
            dias_vencidos = date.today()-ar.fecha_vencimiento
            ArchivoTrabajadores.objects.filter(id_archivo_trabajador=ar.id_archivo_trabajador).update(dias_restantes=str(dias_vencidos.days))
            count+=1
            
            messages.warning(request,"archivos vencidos "+ str(count) )
    data = {}
    
    fecha_hoy=date.today()
    data["fecha_hoy"]=fecha_hoy
    count=0
    
    data["entity_archivo"]= archivos
    return render(request, 'app/dashboard/archivo-trabajador/archivos.html',data)