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
def agregar_trabajos(request, id_trabajador):
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
        #print(request.POST)
        result = 0
        data_trabajos = {
            'id_empresa': id_empresa,
            'id_trabajador':id_trabajador,
            'tipo_trabajo':request.POST['tipo_trabajo'],
            'fecha_realizacion':request.POST['fecha_realizacion'],
            'fecha_vencimiento':request.POST['fecha_vencimiento']
        }
        formulario_trabajos = TrabajosForm(data = data_trabajos)
        if formulario_trabajos.is_valid():
            formulario_trabajos.save() 
            result = 1
            # login(request, user)
        if result == 1:
            messages.success(request, "Solicitud de contacto enviada correctamente.")
            return redirect (to="trabajos")
        else:
            messages.error(request, "error.")

    return render(request, 'app/dashboard/trabajos-capacitacion/agregar-trabajos.html', data) 

def agregar_capacitacion(request, id_trabajador):
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
        #print(request.POST)
        result = 0
        data_capacitacion = {
            'id_empresa': id_empresa,
            'id_trabajador':id_trabajador,
            'tipo_capacitacion':request.POST['tipo_capacitacion'],
            'fecha_realizacion':request.POST['fecha_realizacion'],
            'fecha_vencimiento':request.POST['fecha_vencimiento']
        }
        formulario_capacitacion = CapacitacionForm(data = data_capacitacion)
        if formulario_capacitacion.is_valid():
            formulario_capacitacion.save() 
            result = 1
            # login(request, user)
        if result == 1:
            messages.success(request, "Solicitud de contacto enviada correctamente.")
            return redirect (to="capacitacion")
        else:
            messages.error(request, "error.")

    return render(request, 'app/dashboard/trabajos-capacitacion/agregar-capacitacion.html', data) 

def listar_capacitacion(request):
    data = {}
    capaitacion = Capacitacion.objects.all()
    data["entity_capacitacion"]= capaitacion
    
    return render(request, 'app/dashboard/trabajos-capacitacion/listar-capacitacion.html',data)

@login_required
def listar_empresas(request):
    data = {}
    empresa = Empresa.objects.all()
    data["entity_empresa"]= empresa
    
    return render(request, 'app/dashboard/trabajos-capacitacion/listado-empresas.html',data)

def listar_trabajos(request):
    data = {}
    trabajos = Trabajos.objects.all()
    data["entity_trabajos"]= trabajos
    
    return render(request, 'app/dashboard/trabajos-capacitacion/listar-trabajos.html',data)

@login_required
def vista_trabajadores(request, id_empresa):
    trabajadores = Trabajadores.objects.filter(id_empresa = id_empresa)

    data = {
        'trabajadores':trabajadores
    }

    return render(request, 'app/dashboard/trabajos-capacitacion/listado-trabajadores.html', data)

@login_required
def trabajos_edit(request, id_trabajos):
    trabajos_intancia = get_object_or_404(Trabajos, id_trabajos=id_trabajos)
    trabajos = Trabajos.objects.filter(id_trabajos = id_trabajos)
    
    for tbj in trabajos:
        print(tbj.id_empresa)
        empresa= Empresa.objects.filter(razon_social= tbj.id_empresa)
        trabajador = Trabajadores.objects.filter(nombre_trabajador = tbj.id_trabajador)
        for emp in empresa:
            id_empresa =emp.id_empresa 

        for trab in trabajador:
            id_trabajador = trab.id_trabajador
    result = 0
    if request.method == 'POST':
        print(request.POST)
        data_trabajos = {
            'id_empresa': id_empresa,
            'id_trabajador':id_trabajador,
            'tipo_trabajo':request.POST['tipo_trabajo'],
            'fecha_realizacion':request.POST['fecha_realizacion'],
            'fecha_vencimiento':request.POST['fecha_vencimiento']
        }
        result=1
        formulario_trabajos= TrabajosForm(data = data_trabajos , instance=trabajos_intancia)
        if formulario_trabajos.is_valid():
            
            formulario_trabajos.save()
        else:
            result = 0
        if result == 1:
            messages.success(request, "Solicitud de contacto enviada correctamente.")
            return redirect (to="trabajos")
        else:
            messages.error(request, "error.")
    
    data = {
        'trabajos':trabajos
    }
    return render(request, "app/dashboard/trabajos-capacitacion/editar-trabajos.html",data)

@login_required
def capacitacion_edit(request, id_capacitacion):
    capacitacion_intancia = get_object_or_404(Capacitacion, id_capacitacion=id_capacitacion)
    capacitacion = Capacitacion.objects.filter(id_capacitacion = id_capacitacion)
    
    for cap in capacitacion:
        print(cap.id_empresa)
        empresa= Empresa.objects.filter(razon_social= cap.id_empresa)
        trabajador = Trabajadores.objects.filter(nombre_trabajador = cap.id_trabajador)
        for emp in empresa:
            id_empresa =emp.id_empresa 

        for trab in trabajador:
            id_trabajador = trab.id_trabajador
    result = 0
    if request.method == 'POST':
        print(request.POST)
        data_capacitacion = {
            'id_empresa': id_empresa,
            'id_trabajador':id_trabajador,
            'tipo_capacitacion':request.POST['tipo_capacitacion'],
            'fecha_realizacion':request.POST['fecha_realizacion'],
            'fecha_vencimiento':request.POST['fecha_vencimiento']
        }
        result=1
        formulario_capacitacion= CapacitacionForm(data = data_capacitacion , instance=capacitacion_intancia)
        if formulario_capacitacion.is_valid():
            
            formulario_capacitacion.save()
        else:
            result = 0
        if result == 1:
            messages.success(request, "Solicitud de contacto enviada correctamente.")
            return redirect (to="capacitacion")
        else:
            messages.error(request, "error.")
    
    data = {
        'capacitacion':capacitacion
    }
    return render(request, "app/dashboard/trabajos-capacitacion/editar-capacitacion.html",data)

@login_required   
def eliminar_trabajos(request,id_trabajos):
    trabajos = get_object_or_404(Trabajos, id_trabajos=id_trabajos)
    trabajos.delete()
    messages.success(request, "Trabajo eliminada correctamente")
    return redirect(to="trabajos")

@login_required
def eliminar_capacitacion(request,id_capacitacion):
    capacitacion = get_object_or_404(Capacitacion, id_capacitacion=id_capacitacion)
    capacitacion.delete()
    messages.success(request, "Capacitacion eliminada correctamente")
    return redirect(to="capacitacion")