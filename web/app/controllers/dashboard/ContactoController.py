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
def listar_contactos(request):
    data = {}
    contacto_empresa = ContactoEmpresa.objects.all()
    data["entity_contacto"]= contacto_empresa
    return render(request, 'app/dashboard/contacto/contactos.html',data)
    
@login_required
def contacto_edit(request, id_contacto):
    contacto_intancia = get_object_or_404(ContactoEmpresa, id_contacto=id_contacto)
    contacto = ContactoEmpresa.objects.filter(id_contacto = id_contacto)
    
    for con in contacto:
        print(con.id_empresa)
        empresa= Empresa.objects.filter(razon_social= con.id_empresa)
        for emp in empresa:
            id_empresa =emp.id_empresa    
    result = 0
    if request.method == 'POST':
        print(request.POST)
        data_contacto = {
            'nombre_contacto':request.POST['nombre_contacto'],
            'rut_contacto':request.POST['rut_contacto'],
            'telefono_contacto':request.POST['telefono_contacto'],
            'cargo_contacto':request.POST['cargo_contacto'],
            'correo':request.POST['correo'],
            'id_empresa':id_empresa
        } 
        result=1
        formulario_contacto= ContactoEmpresaForm(data = data_contacto , instance=contacto_intancia)
        if formulario_contacto.is_valid():
            
            formulario_contacto.save()
        else:
            result = 0
        if result == 1:
            messages.success(request, "Solicitud de contacto enviada correctamente.")
            return redirect (to="contactos")
        else:
            messages.error(request, "error.")
    
    data = {
        'contacto':contacto
    }
    return render(request, "app/dashboard/contacto/editar-contacto.html",data)

@login_required
def eliminar_contacto(request,id_contacto):
    contacto = get_object_or_404(ContactoEmpresa, id_contacto=id_contacto)
    contacto.delete()
    messages.success(request, "Contacto eliminada correctamente")
    return redirect(to="contactos")