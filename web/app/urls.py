from django.urls import path
from .controllers.home.HomeController import *
from .controllers.dashboard.UsuarioController import *
from .controllers.dashboard.EmpresasController import *
from .controllers.dashboard.TrabajadoresController import *
from .controllers.dashboard.ContactoController import *
from .controllers.dashboard.AchsGestionController import *
from .controllers.dashboard.TrabajosNuevosController import *
from .controllers.dashboard.OAController import *
from .controllers.dashboard.ProtocoloController import *
from .controllers.dashboard.CapacitacionController import *

urlpatterns = [
    #Home
    path('', home , name="home"),
    path('sobre-nosotros/', about , name="about"),
    path('contacto/', contacto , name="contacto"),
    # Usuarios
    path('usuarios/', listar_usuarios, name="usuarios"),
    path('agregar-usuario/', agregar_usuario, name="agregar-usuario"),
    #Empresas
    path('empresas/', listar_empresas, name="empresas"),
    path('agregar-empresa/', agregar_empresa, name="agregar-empresa"),
    #Trabajadores
    path('trabajadores/', listar_trabajadores, name="trabajadores"),
    path('agregar-trabajador/', agregar_trabajador, name="agregar-trabajador"),
    #Contacto
    path('contactos/', listar_contactos, name="contactos"),
    path('agregar-contacto/', agregar_contacto, name="agregar-contacto"),
    #AchsGestion
    path('gestiones/', listar_gestiones, name="gestiones"),
    path('agregar-gestion/', agregar_gestion, name="agregar-gestion"),
    #Trabajos
    path('trabajos/', listar_trabajos, name="trabajos"),
    path('agregar-trabajos/', agregar_trabajos, name="agregar-trabajos"),
    #OA
    path('oa/', listar_oa, name="oa"),
    path('agregar-oa/', agregar_oa, name="agregar-oa"),
    #Capacitacion
    path('capacitaciones/', listar_capacitacion, name="capacitaciones"),
    path('agregar-capacitacion/', agregar_capacitacion, name="agregar-capacitacion"),
    #Protocolo
    path('protocolo/', listar_protocolo, name="protocolo"),
    path('agregar-protocolo/', agregar_protocolo, name="agregar-protocolo"),
    
]