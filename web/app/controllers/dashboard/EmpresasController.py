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
def agregar_empresa(request):

    if request.method == 'POST':
        print(request.POST)
        result = 0
        data_empresa = {
            'razon_social':request.POST['razon_social'],
            'rut_empresa':request.POST['rut_empresa'],
            'direccion':request.POST['direccion'],
            'ct':request.POST['ct'],
            'clave_seremi':request.POST['clave_seremi']
        }
        formulario_empresa = EmpresaForm(data = data_empresa)
        if formulario_empresa.is_valid():
            formulario_empresa.save() 
            rut = Empresa.objects.filter(rut_empresa=request.POST['rut_empresa'])
            for n in rut:
                id_empresa= n.id_empresa
                
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
                'id_empresa': id_empresa
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
                'id_empresa': id_empresa
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
def listar_empresas(request):
    empresa = Empresa.objects.all()
    contacto = ContactoEmpresa.objects.all()
    oa = Oa.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(empresa, 100)
        empresa = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': empresa,
        'paginator': paginator
    }
    return render(request, 'app/dashboard/empresas/empresas.html', data)