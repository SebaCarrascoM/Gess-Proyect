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
    path('empresa-eliminar/<int:id_empresa>', eliminar_empresa, name="empresa-eliminar"),
    #Trabajadores
    path('trabajadores/', listar_trabajadores, name="trabajadores"),
    path('agregar-trabajador/<int:id_empresa>', agregar_trabajador, name="agregar-trabajador"),
    path('trabajador-edit/<int:id_trabajador>', trabajadores_edit, name="trabajador-edit"),
    path('trabajador-eliminar/<int:id_trabajador>', eliminar_trabajador, name="trabajador-eliminar"),
    #Contacto
    path('contactos/', listar_contactos, name="contactos"),
    path('contacto-edit/<int:id_contacto>', contacto_edit, name="contacto-edit"),
    path('contacto-eliminar/<int:id_contacto>', eliminar_contacto, name="contacto-eliminar"),
    #AchsGestion
    path('gestiones/', listar_gestiones, name="gestiones"),
    path('agregar-gestion/<int:id_empresa>', agregar_gestion, name="agregar-gestion"),
    path('achs-edit/<int:id_achs_gestion>', achs_edit, name="achs-edit"),
    path('achs-eliminar/<int:id_achs_gestion>', eliminar_achs, name="achs-eliminar"),
    #Trabajo-capacitacion
    path('empresas-trabajos/', listar_empresas, name="empresas-trabajos"),
    path('agregar-trabajos/<int:id_trabajador>', agregar_trabajos, name="agregar-trabajos"),
    path('listado-trabajadores/<int:id_empresa>', vista_trabajadores, name="listado-trabajadores"),
    path('trabajos/', listar_trabajos, name="trabajos"),
    path('agregar-capacitacion/<int:id_trabajador>', agregar_capacitacion, name="agregar-capacitacion"),
    path('capacitacion/', listar_capacitacion, name="capacitacion"),
    path('capacitacion-edit/<int:id_capacitacion>', capacitacion_edit, name="capacitacion-edit"),
    path('trabajos-edit/<int:id_trabajos>', trabajos_edit, name="trabajos-edit"),
    path('capacitacion-eliminar/<int:id_capacitacion>', eliminar_capacitacion, name="capacitacion-eliminar"),
    path('trabajos-eliminar/<int:id_trabajos>', eliminar_trabajos, name="trabajos-eliminar"),
    #OA
    path('oa/', listar_oa, name="oa"),
    path('oa-edit/<int:id_oa>', oa_edit, name="oa-edit"),
    path('oa-eliminar/<int:id_oa>', eliminar_oa, name="oa-eliminar"),
    #Protocolo
    path('protocolo/', listar_protocolo, name="protocolo"),
    path('agregar-protocolo/<int:id_empresa>', agregar_protocolo, name="agregar-protocolo"),
    path('protocolo-edit/<int:id_protocolo>', protocolo_edit, name="protocolo-edit"),
    path('protocolo-eliminar/<int:id_protocolo>', eliminar_protocolo, name="protocolo-eliminar"),
    #ArchivosEmpresa
    path('agregar-archivo-empresa/<int:id_empresa>', agregar_archivo_empresa, name="agregar-archivo-empresa"),
    path('archivos/', listar_archivos, name="archivos"),
    path('archivo-empresa-eliminar/<int:id_documento_empresa>', eliminar_archivo_empresa, name="archivo-empresa-eliminar"),
    path('archivo-empresa-edit/<int:id_documento_empresa>', archivo_empresa_edit, name="archivo-empresa-edit"),
    #ArchivoTrabajador
    path('agregar-archivo-trabajador/<int:id_trabajador>', agregar_archivo_trabajador, name="agregar-archivo-trabajador"),
    path('archivos-trabajador/', listar_archivos_trabajador, name="archivos-trabajador"),
    path('archivo-trabajador-eliminar/<int:id_archivo_trabajador>', eliminar_archivo_trabajador, name="archivo-trabajador-eliminar"),
    path('archivo-trabajador-edit/<int:id_archivo_trabajador>', archivo_trabajador_edit, name="archivo-trabajador-edit"),
]