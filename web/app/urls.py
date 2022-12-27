from django.urls import path
from .controllers.home.HomeController import *
from .controllers.dashboard.UsuarioController import *
from .controllers.dashboard.EmpresasController import *

urlpatterns = [
    path('', home , name="home"),
    path('sobre-nosotros/', about , name="about"),
    path('contacto/', contacto , name="contacto"),
    # USUARIOS
    path('usuarios/', listar_usuarios, name="usuarios"),
    path('agregar-usuario/', agregar_usuario, name="agregar-usuario"),
    #Empresas
    path('empresas/', listar_empresas, name="empresas"),
]