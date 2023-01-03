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
        

    return render(request, 'app/dashboard/empresas/agregar-empresa.html') 

@login_required
def listar_empresas(request):
    # empresa = AuthUser.objects.all()
    # page = request.GET.get('page', 1)
    
    # try:
    #     paginator = Paginator(empresa, 5)
    #     empresa = paginator.page(page)
    # except:
    #     raise Http404
    
    # data = {
    #     'entity': empresa,
    #     'paginator': paginator
    # }
    
    return render(request, 'app/dashboard/empresas/empresas.html')