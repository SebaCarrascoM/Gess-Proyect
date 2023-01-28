from django.shortcuts import render, redirect
from django.contrib import messages
from ...forms import *
from ...models import *
from ...functions import *
import requests
from datetime import datetime
from django.utils import timezone
# Create your views here.


def calendario(request):

    return render(request, 'app/dashboard/calendario/calendario.html')