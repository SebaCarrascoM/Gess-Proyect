from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from ...forms import *
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.http import Http404
from django.utils import timezone
# Create your views here.

@login_required
def agregar_trabajador(request):

    if request.method == 'POST':
        print(request.POST)
        result = 0
        fecha_actual = timezone.now()
        formulario_trabajador = {
            'empresa':request.POST['empresa'],
            'nombre_trabajador':request.POST['nombre_trabajador'],
            'rut_trabajador':request.POST['rut_trabajador'],
            'direccion_trabajador':request.POST['direccion_trabajador'],
            'email_trabajador':request.POST['email_trabajador'],
            'cargo':request.POST['cargo'],
            'area':request.POST['area'],
            'fecha_nacimiento':request.POST['fecha_nacimiento'],
            'fecha_ingreso':fecha_actual
        }
        formulario_trabajador = TrabajadoresForm(data = formulario_trabajador)
        if formulario_trabajador.is_valid():
            formulario_trabajador.save()
        else:
            result = 0
        if result == 1:
            messages.success(request, "Solicitud de contacto enviada correctamente.")
            return redirect (to="trabajadores")
        else:
            messages.error(request, "error.")


    return render(request, 'app/dashboard/trabajadores/agregar-trabajador.html') 

@login_required
def listar_trabajadores(request):
    trabajadores = Trabajadores.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(trabajadores, 5)
        trabajadores = paginator.page(page)
    except:
        raise Http404
    
    data = {
        'entity': trabajadores,
        'paginator': paginator
    }
    
    return render(request, 'app/dashboard/trabajadores/trabajadores.html')