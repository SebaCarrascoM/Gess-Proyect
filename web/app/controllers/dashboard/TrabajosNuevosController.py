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
def agregar_trabajos(request):

    if request.method == 'POST':
        print(request.POST)
        formulario = EmpresaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            # login(request, user)
            messages.success(request, "Trabajo Creado Exitosamente")
            return redirect(to="trabajos")

    return render(request, 'app/dashboard/trabajos-nuevos/agregar-trabajos.html') 

@login_required
def listar_trabajos(request):
    trabajos_nuevos = TrabajosNuevos.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(trabajos_nuevos, 5)
        trabajos_nuevos = paginator.page(page)
    except:
        raise Http404
    
    data = {
        'entity': trabajos_nuevos,
        'paginator': paginator
    }
    
    return render(request, 'app/dashboard/trabajos-nuevos/trabajos.html',data)