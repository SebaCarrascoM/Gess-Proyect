from django.urls import path
from .controllers.home.HomeController import *
from .controllers.dashboard.UsuarioController import *
from .controllers.dashboard.EmpresasController import *
from .controllers.dashboard.TrabajadoresController import *
from .controllers.dashboard.ContactoController import *
from .controllers.dashboard.AchsGestionController import *
from .controllers.dashboard.TrabajosCapacitacionController import *
from .controllers.dashboard.OAController import *
from .controllers.dashboard.ProtocoloController import *
from .controllers.dashboard.CalendarioController import *
from .controllers.dashboard.ArchivoEmpresaController import *
from .controllers.dashboard.ArchivoTrabajadorController import *

urlpatterns = [
    #Home
    path('', home , name="home"),
    path('sobre-nosotros/', about , name="about"),
    path('contacto/', contacto , name="contacto"),
    path('inicio/', inicio , name="inicio"),
    path('calendario/', calendario , name="calendario"),
    # Usuarios
    path('usuarios/', listar_usuarios, name="usuarios"),
    path('agregar-usuario/', agregar_usuario, name="agregar-usuario"),
    #Empresas
    path('empresas/', listar_empresa, name="empresas"),
    path('agregar-empresa/', agregar_empresa, name="agregar-empresa"),
    path('empresa-edit/<int:id_empresa>', empresa_edit, name="empresa-edit"),
    path('gestor-empresas/', gestion_empresa, name="gestor-empresas"),
    #Trabajadores
    path('trabajadores/', listar_trabajadores, name="trabajadores"),
    path('agregar-trabajador/<int:id_empresa>', agregar_trabajador, name="agregar-trabajador"),
    #Contacto
    path('contactos/', listar_contactos, name="contactos"),
    #AchsGestion
    path('gestiones/', listar_gestiones, name="gestiones"),
    path('agregar-gestion/<int:id_empresa>', agregar_gestion, name="agregar-gestion"),
    #Trabajo-capacitacion
    path('empresas-trabajos/', listar_empresas, name="empresas-trabajos"),
    path('agregar-trabajos/<int:id_trabajador>', agregar_trabajos, name="agregar-trabajos"),
    path('listado-trabajadores/<int:id_empresa>', vista_trabajadores, name="listado-trabajadores"),
    path('trabajos/', listar_trabajos, name="trabajos"),
    path('agregar-capacitacion/<int:id_trabajador>', agregar_capacitacion, name="agregar-capacitacion"),
    path('capacitacion/', listar_capacitacion, name="capacitacion"),
    #OA
    path('oa/', listar_oa, name="oa"),
    #Protocolo
    path('protocolo/', listar_protocolo, name="protocolo"),
    path('agregar-protocolo/<int:id_empresa>', agregar_protocolo, name="agregar-protocolo"),
    #ArchivosEmpresa
    path('agregar-archivo-empresa/<int:id_empresa>', agregar_archivo_empresa, name="agregar-archivo-empresa"),
    path('archivos/', listar_archivos, name="archivos"),
    #ArchivoTrabajador
    path('agregar-archivo-trabajador/<int:id_trabajador>', agregar_archivo_trabajador, name="agregar-archivo-trabajador"),
    path('archivos-trabajador/', listar_archivos_trabajador, name="archivos-trabajador"),
]