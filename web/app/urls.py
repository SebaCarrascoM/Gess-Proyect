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
    path('trabajador-edit/<int:id_trabajador>', trabajadores_edit, name="trabajador-edit"),
    #Contacto
    path('contactos/', listar_contactos, name="contactos"),
    path('contacto-edit/<int:id_contacto>', contacto_edit, name="contacto-edit"),
    #AchsGestion
    path('gestiones/', listar_gestiones, name="gestiones"),
    path('agregar-gestion/<int:id_empresa>', agregar_gestion, name="agregar-gestion"),
    path('achs-edit/<int:id_achs_gestion>', achs_edit, name="achs-edit"),
    #Trabajo-capacitacion
    path('empresas-trabajos/', listar_empresas, name="empresas-trabajos"),
    path('agregar-trabajos/<int:id_trabajador>', agregar_trabajos, name="agregar-trabajos"),
    path('listado-trabajadores/<int:id_empresa>', vista_trabajadores, name="listado-trabajadores"),
    path('trabajos/', listar_trabajos, name="trabajos"),
    path('agregar-capacitacion/<int:id_trabajador>', agregar_capacitacion, name="agregar-capacitacion"),
    path('capacitacion/', listar_capacitacion, name="capacitacion"),
    path('capacitacion-edit/<int:id_protocolo>', capacitacion_edit, name="capacitacion-edit"),
    path('trabajos-edit/<int:id_protocolo>', trabajos_edit, name="trabajos-edit"),
    #OA
    path('oa/', listar_oa, name="oa"),
    path('oa-edit/<int:id_oa>', oa_edit, name="oa-edit"),
    #Protocolo
    path('protocolo/', listar_protocolo, name="protocolo"),
    path('agregar-protocolo/<int:id_empresa>', agregar_protocolo, name="agregar-protocolo"),
    path('protocolo-edit/<int:id_protocolo>', protocolo_edit, name="protocolo-edit"),
    #ArchivosEmpresa
    path('agregar-archivo-empresa/<int:id_empresa>', agregar_archivo_empresa, name="agregar-archivo-empresa"),
    path('archivos/', listar_archivos, name="archivos"),
    #ArchivoTrabajador
    path('agregar-archivo-trabajador/<int:id_trabajador>', agregar_archivo_trabajador, name="agregar-archivo-trabajador"),
    path('archivos-trabajador/', listar_archivos_trabajador, name="archivos-trabajador"),
]