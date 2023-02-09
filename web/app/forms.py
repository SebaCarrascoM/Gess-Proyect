from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import *
from django import forms
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = "__all__"

class ContactoEmpresaForm(forms.ModelForm):
    class Meta:
        model = ContactoEmpresa
        fields = "__all__"

class AchsGestionForm(forms.ModelForm):
    class Meta:
        model = AchsGestion
        fields = "__all__"

class ArchivoEmpresaForm(forms.ModelForm):
    class Meta:
        model = ArchivoEmpresa
        fields = "__all__" 

class ArchivoTrabajadorForm(forms.ModelForm):
    class Meta:
        model = ArchivoTrabajadores
        fields = "__all__" 

class CapacitacionForm(forms.ModelForm):
    class Meta:
        model = Capacitacion
        fields = "__all__"

class OaForm(forms.ModelForm):
    class Meta:
        model = Oa
        fields = "__all__"

class ProtocoloForm(forms.ModelForm):
    class Meta:
        model = Protocolo
        fields = "__all__"

class TrabajadoresForm(forms.ModelForm):
    class Meta:
        model = Trabajadores
        fields = "__all__"

class TrabajosForm(forms.ModelForm):
    class Meta:
        model = Trabajos
        fields = "__all__"