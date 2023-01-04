from django.db import models

class AchsGestion(models.Model):
    id_achs_gestion = models.AutoField(primary_key=True)
    tipo_requisito = models.CharField(max_length=50)
    accion = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    observaciones = models.CharField(max_length=100)
    id_empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='id_empresa')

    class Meta:
        managed = False
        db_table = 'achs_gestion'


class ArchivoEmpresa(models.Model):
    id_documento_empresa = models.AutoField(primary_key=True)
    documentos = models.CharField(max_length=100)
    fecha_apliacion = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    observaciones = models.TextField()
    id_empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='id_empresa')

    class Meta:
        managed = False
        db_table = 'archivo_empresa'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Capacitacion(models.Model):
    id_capacitacion = models.AutoField(primary_key=True)
    id_trabajador = models.ForeignKey('Trabajadores', models.DO_NOTHING, db_column='id_trabajador')
    tipo_capacitacion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'capacitacion'


class ContactoEmpresa(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    nombre_contacto = models.CharField(max_length=50)
    rut_contacto = models.CharField(max_length=13)
    cargo_contacto = models.CharField(max_length=50)
    telefono_contacto = models.CharField(max_length=13)
    correo = models.CharField(max_length=50)
    id_empresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='id_empresa')

    class Meta:
        managed = False
        db_table = 'contacto_empresa'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    razon_social = models.CharField(max_length=50)
    rut_empresa = models.CharField(max_length=13)
    direccion = models.CharField(max_length=50)
    ct = models.CharField(max_length=50)
    clave_seremi = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'empresa'


class Oa(models.Model):
    id_oa = models.AutoField(primary_key=True)
    usuario_web = models.CharField(max_length=50)
    clave_web = models.CharField(max_length=50)
    asesor_oa = models.CharField(max_length=50)
    telefono = models.CharField(max_length=14)
    correo_oa = models.CharField(max_length=50)
    id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='id_empresa')

    class Meta:
        managed = False
        db_table = 'oa'


class Protocolo(models.Model):
    id_protocolo = models.AutoField(primary_key=True)
    nombre_protocolo = models.CharField(max_length=50)
    requisito = models.CharField(max_length=50)
    evidencia = models.CharField(max_length=50)
    fecha_realizacion = models.DateField()
    proxima_aplicacion = models.DateField()
    id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='id_empresa')

    class Meta:
        managed = False
        db_table = 'protocolo'


class Trabajadores(models.Model):
    id_trabajador = models.AutoField(primary_key=True)
    nombre_trabajador = models.CharField(max_length=50)
    rut_trabajador = models.CharField(max_length=13)
    cargo = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    telefono_trabajador = models.CharField(max_length=13)
    email_trabajador = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()
    direccion_trabajador = models.CharField(max_length=50)
    id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='id_empresa')

    class Meta:
        managed = False
        db_table = 'trabajadores'


class TrabajosNuevos(models.Model):
    id_trabajos_nuevos = models.AutoField(primary_key=True)
    id_trabajador = models.ForeignKey(Trabajadores, models.DO_NOTHING, db_column='id_trabajador')
    tipo_trabajo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'trabajos_nuevos'