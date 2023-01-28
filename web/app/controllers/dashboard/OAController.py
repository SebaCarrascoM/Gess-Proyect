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
def listar_oa(request):
    data = {}
    oa = Oa.objects.all()
    data["entity_oa"]= oa
    
    return render(request, 'app/dashboard/oa/oa.html',data)