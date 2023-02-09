from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
import requests
from ...forms import *
from ...models import *
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.

@login_required
def agregar_empresa(request):
    
    if request.method == 'POST':
        #print(request.POST)
        result = 0
        data_empresa = {
            'razon_social':request.POST['razon_social'],
            'rut_empresa':request.POST['rut_empresa'],
            'direccion':request.POST['direccion'],
            'ct':request.POST['ct'],
            'clave_seremi':request.POST['clave_seremi'],
            'seguro_laboral':request.POST['seguro_laboral'],
            'nro_trabajadores':request.POST['nro_trabajadores']
            
        }
        formulario_empresa = EmpresaForm(data = data_empresa)

        if formulario_empresa.is_valid():

            formulario_empresa.save() 
            rut = Empresa.objects.filter(rut_empresa=request.POST['rut_empresa'])
            print(rut)
            for n in rut:
                id_empresa = n.id_empresa
                print(id_empresa)
            result = 1
            print(id_empresa)
        else:
            result = 0
        
        valida_contacto = request.POST['valida_contacto']
        valida_oa = request.POST['valida_oa']

        if valida_contacto == '1':
            data_contacto = {
                'nombre_contacto':request.POST['nombre_contacto'],
                'rut_contacto':request.POST['rut_contacto'],
                'telefono_contacto':request.POST['telefono_contacto'],
                'cargo_contacto':request.POST['cargo_contacto'],
                'correo':request.POST['correo'],
                'id_empresa':id_empresa
            }
            formulario_contacto = ContactoEmpresaForm(data = data_contacto)
            
            if formulario_contacto.is_valid():
                formulario_contacto.save() 
                result = 1
            else:
                result = 0
        if valida_oa == '1':

            data_oa = {
                'usuario_web':request.POST['usuario_web'],
                'clave_web':request.POST['clave_web'],
                'asesor_oa':request.POST['asesor_oa'],
                'telefono':request.POST['telefono'],
                'correo_oa':request.POST['correo_oa'],
                'id_empresa':id_empresa
            }
            print(data_oa)
            formulario_oa = OaForm(data = data_oa)
            if formulario_oa.is_valid():
                formulario_oa.save()
                result = 1
            else:
                result = 0

        if result == 1:
            messages.success(request, "Solicitud de contacto enviada correctamente.")
            return redirect (to="empresas")
        else:
            messages.error(request, "error.")
    return render(request, 'app/dashboard/empresas/agregar-empresa.html') 

@login_required
def listar_empresa(request):
    data = {}
    empresas = Empresa.objects.all()
    data["entity_empresa"]= empresas
    return render(request, 'app/dashboard/empresas/empresas.html', data)
    
@login_required
def gestion_empresa(request):
    data = {}
    empresas = Empresa.objects.all()
    data["entity_empresa"]= empresas
    return render(request, 'app/dashboard/empresas/gestor-datos.html', data)

@login_required
def empresa_edit(request, id_empresa):
    empresa_intancia = get_object_or_404(Empresa, id_empresa=id_empresa)
    empresa = Empresa.objects.filter(id_empresa = id_empresa)
    data = {
        'empresa':empresa
    }
    result = 0
    if request.method == 'POST':
        print(request.POST)
        result=1
        formulario_empresa = EmpresaForm(data = request.POST , instance=empresa_intancia)
        if formulario_empresa.is_valid():
            formulario_empresa.save()
        else:
            result = 0
        if result == 1:
            messages.success(request, "Solicitud de contacto enviada correctamente.")
            return redirect (to="empresas")
        else:
            messages.error(request, "error.")
    return render(request, "app/dashboard/empresas/empresa-edit.html",data)