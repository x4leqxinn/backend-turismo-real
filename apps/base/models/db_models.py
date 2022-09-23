# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Acompaniante(models.Model):
    id = models.OneToOneField('Persona', models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'acompaniante'


class AdminInterfaceTheme(models.Model):
    name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    active = models.BooleanField()
    title = models.CharField(max_length=50, blank=True, null=True)
    title_visible = models.BooleanField()
    logo = models.CharField(max_length=100, blank=True, null=True)
    logo_visible = models.BooleanField()
    css_header_background_color = models.CharField(max_length=10, blank=True, null=True)
    title_color = models.CharField(max_length=10, blank=True, null=True)
    css_header_text_color = models.CharField(max_length=10, blank=True, null=True)
    css_header_link_color = models.CharField(max_length=10, blank=True, null=True)
    css_header_link_hover_color = models.CharField(max_length=10, blank=True, null=True)
    css_module_background_color = models.CharField(max_length=10, blank=True, null=True)
    css_module_text_color = models.CharField(max_length=10, blank=True, null=True)
    css_module_link_color = models.CharField(max_length=10, blank=True, null=True)
    css_module_link_hover_color = models.CharField(max_length=10, blank=True, null=True)
    css_module_rounded_corners = models.BooleanField()
    css_generic_link_color = models.CharField(max_length=10, blank=True, null=True)
    css_generic_link_hover_color = models.CharField(max_length=10, blank=True, null=True)
    css_save_button_background99e4 = models.CharField(max_length=10, blank=True, null=True)
    css_save_button_background20f4 = models.CharField(max_length=10, blank=True, null=True)
    css_save_button_text_color = models.CharField(max_length=10, blank=True, null=True)
    css_delete_button_backgroue0b7 = models.CharField(max_length=10, blank=True, null=True)
    css_delete_button_backgroua080 = models.CharField(max_length=10, blank=True, null=True)
    css_delete_button_text_color = models.CharField(max_length=10, blank=True, null=True)
    list_filter_dropdown = models.BooleanField()
    related_modal_active = models.BooleanField()
    related_modal_background_color = models.CharField(max_length=10, blank=True, null=True)
    related_modal_rounded_corners = models.BooleanField()
    logo_color = models.CharField(max_length=10, blank=True, null=True)
    recent_actions_visible = models.BooleanField()
    favicon = models.CharField(max_length=100, blank=True, null=True)
    related_modal_background_oe111 = models.CharField(max_length=5, blank=True, null=True)
    env_name = models.CharField(max_length=50, blank=True, null=True)
    env_visible_in_header = models.BooleanField(blank=True, null=True)
    env_color = models.CharField(max_length=10, blank=True, null=True)
    env_visible_in_favicon = models.BooleanField()
    related_modal_close_button3b73 = models.BooleanField()
    language_chooser_active = models.BooleanField()
    language_chooser_display = models.CharField(max_length=10, blank=True, null=True)
    list_filter_sticky = models.BooleanField()
    form_pagination_sticky = models.BooleanField()
    form_submit_sticky = models.BooleanField()
    css_module_background_sele1a15 = models.CharField(max_length=10, blank=True, null=True)
    css_module_link_selected_color = models.CharField(max_length=10, blank=True, null=True)
    logo_max_height = models.IntegerField()
    logo_max_width = models.IntegerField()
    foldable_apps = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'admin_interface_theme'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

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
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUserAccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=254, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    person = models.OneToOneField('Persona', models.DO_NOTHING, blank=True, null=True)
    role = models.ForeignKey('AuthUserRole', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user_account'


class AuthUserAccountGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUserAccount, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_account_groups'
        unique_together = (('user', 'group'),)


class AuthUserAccountUserPerdf00(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUserAccount, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_account_user_perdf00'
        unique_together = (('user', 'permission'),)


class AuthUserRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user_role'


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUserAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Cargo(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cargo'


class Categoria(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    id_sub = models.ForeignKey('SubCategoria', models.DO_NOTHING, db_column='id_sub')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'categoria'


class CheckIn(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha_llegada = models.DateField()
    hora_llegada = models.CharField(max_length=5)
    firma = models.CharField(max_length=1)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()
    id_res = models.OneToOneField('Reserva', models.DO_NOTHING, db_column='id_res')
    id_rec = models.ForeignKey('Recepcionista', models.DO_NOTHING, db_column='id_rec')

    class Meta:
        managed = False
        db_table = 'check_in'


class CheckOut(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha_salida = models.DateField()
    hora_salida = models.CharField(max_length=5, blank=True, null=True)
    total_multa = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()
    id_rec = models.ForeignKey('Recepcionista', models.DO_NOTHING, db_column='id_rec')
    id_res = models.OneToOneField('Reserva', models.DO_NOTHING, db_column='id_res')

    class Meta:
        managed = False
        db_table = 'check_out'


class Ciudad(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_est = models.ForeignKey('EstadoPais', models.DO_NOTHING, db_column='id_est')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ciudad'


class CliAcom(models.Model):
    id = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()
    id_res = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='id_res')
    id_aco = models.ForeignKey(Acompaniante, models.DO_NOTHING, db_column='id_aco')
    id_cli = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cli')

    class Meta:
        managed = False
        db_table = 'cli_acom'


class CliCom(models.Model):
    id = models.IntegerField(primary_key=True)
    id_cli = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cli')
    id_viv = models.ForeignKey('Vivienda', models.DO_NOTHING, db_column='id_viv')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cli_com'


class Cliente(models.Model):
    id = models.OneToOneField('Persona', models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Color(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'color'


class Comentario(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    id_cli = models.OneToOneField(CliCom, models.DO_NOTHING, db_column='id_cli')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comentario'


class Conductor(models.Model):
    id = models.OneToOneField('Empleado', models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'conductor'


class DCheck(models.Model):
    id = models.OneToOneField('Documento', models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'd_check'


class DCoordinacion(models.Model):
    id = models.OneToOneField('Documento', models.DO_NOTHING, db_column='id', primary_key=True)
    id_mov = models.OneToOneField('Movilizacion', models.DO_NOTHING, db_column='id_mov')

    class Meta:
        managed = False
        db_table = 'd_coordinacion'


class DatabaseDdl(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=100)
    objeto = models.CharField(max_length=100)
    nom_objeto = models.CharField(max_length=100)
    operacion = models.CharField(max_length=100)
    creacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'database_ddl'


class Destino(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'destino'


class DetServMov(models.Model):
    id = models.IntegerField(primary_key=True)
    id_con = models.ForeignKey(Conductor, models.DO_NOTHING, db_column='id_con')
    id_mov = models.ForeignKey('Movilizacion', models.DO_NOTHING, db_column='id_mov')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'det_serv_mov'


class DetVehMov(models.Model):
    id = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()
    id_veh = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='id_veh')
    id_mov = models.ForeignKey('Movilizacion', models.DO_NOTHING, db_column='id_mov')

    class Meta:
        managed = False
        db_table = 'det_veh_mov'


class DetalleMulta(models.Model):
    id = models.IntegerField(primary_key=True)
    id_mul = models.ForeignKey('Multa', models.DO_NOTHING, db_column='id_mul')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()
    id_che = models.ForeignKey(CheckOut, models.DO_NOTHING, db_column='id_che')

    class Meta:
        managed = False
        db_table = 'detalle_multa'


class DetalleProducto(models.Model):
    id = models.IntegerField(primary_key=True)
    id_est = models.ForeignKey('EstadoProducto', models.DO_NOTHING, db_column='id_est')
    id_det = models.ForeignKey('DetalleSala', models.DO_NOTHING, db_column='id_det')
    id_pro = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_pro')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'detalle_producto'


class DetalleSala(models.Model):
    id = models.IntegerField(primary_key=True)
    id_inv = models.ForeignKey('Inventario', models.DO_NOTHING, db_column='id_inv')
    id_sal = models.ForeignKey('Sala', models.DO_NOTHING, db_column='id_sal')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'detalle_sala'


class DetalleServicio(models.Model):
    id = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()
    id_res = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='id_res')
    id_ser = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_ser')

    class Meta:
        managed = False
        db_table = 'detalle_servicio'


class DetalleTour(models.Model):
    id = models.IntegerField(primary_key=True)
    id_tou = models.ForeignKey('Tour', models.DO_NOTHING, db_column='id_tou')
    id_des = models.ForeignKey(Destino, models.DO_NOTHING, db_column='id_des')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'detalle_tour'


class Disponibilidad(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'disponibilidad'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUserAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DocIdentidad(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=80)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'doc_identidad'


class Documento(models.Model):
    id = models.IntegerField(primary_key=True)
    id_tip = models.ForeignKey('TipoDocumento', models.DO_NOTHING, db_column='id_tip')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'documento'


class Empleado(models.Model):
    id = models.OneToOneField('Persona', models.DO_NOTHING, db_column='id', primary_key=True)
    sueldo = models.IntegerField()
    fecha_contrato = models.DateField()
    id_car = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='id_car')

    class Meta:
        managed = False
        db_table = 'empleado'


class ErrorProceso(models.Model):
    id = models.IntegerField(primary_key=True)
    cod_error = models.CharField(max_length=100)
    subprograma = models.CharField(max_length=100)
    mensaje_error = models.CharField(max_length=300)
    creacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'error_proceso'


class EstadoCivil(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'estado_civil'


class EstadoPais(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    id_pai = models.ForeignKey('Pais', models.DO_NOTHING, db_column='id_pai')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'estado_pais'


class EstadoProducto(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'estado_producto'


class GaleriaExterior(models.Model):
    id = models.IntegerField(primary_key=True)
    imagen = models.TextField()
    id_viv = models.ForeignKey('Vivienda', models.DO_NOTHING, db_column='id_viv')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'galeria_exterior'


class GaleriaInterior(models.Model):
    id = models.IntegerField(primary_key=True)
    imagen = models.TextField()
    id_viv = models.ForeignKey('Vivienda', models.DO_NOTHING, db_column='id_viv')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'galeria_interior'


class Genero(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'genero'


class Inventario(models.Model):
    id = models.IntegerField(primary_key=True)
    id_viv = models.OneToOneField('Vivienda', models.DO_NOTHING, db_column='id_viv')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'inventario'


class Marca(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'marca'


class Modelo(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'modelo'


class Movilizacion(models.Model):
    id = models.OneToOneField('Servicio', models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'movilizacion'


class Multa(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    monto = models.IntegerField()
    id_tip = models.ForeignKey('TipoMulta', models.DO_NOTHING, db_column='id_tip')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'multa'


class Pais(models.Model):
    id = models.CharField(primary_key=True, max_length=4)
    cod_pais = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    cod_tel = models.CharField(max_length=10)
    bandera = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pais'


class Persona(models.Model):
    id = models.BigIntegerField(primary_key=True)
    run = models.CharField(unique=True, max_length=15, blank=True, null=True)
    dv = models.CharField(max_length=1, blank=True, null=True)
    pasaporte = models.CharField(unique=True, max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=50)
    snombre = models.CharField(max_length=50, blank=True, null=True)
    ap_paterno = models.CharField(max_length=50)
    ap_materno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=10)
    num_calle = models.CharField(max_length=10)
    calle = models.CharField(max_length=30)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()
    id_ciu = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciu')
    id_est = models.ForeignKey(EstadoPais, models.DO_NOTHING, db_column='id_est')
    id_pai = models.ForeignKey(Pais, models.DO_NOTHING, db_column='id_pai')
    id_doc = models.ForeignKey(DocIdentidad, models.DO_NOTHING, db_column='id_doc')
    id_est1 = models.ForeignKey(EstadoCivil, models.DO_NOTHING, db_column='id_est1')
    id_gen = models.ForeignKey(Genero, models.DO_NOTHING, db_column='id_gen')

    class Meta:
        managed = False
        db_table = 'persona'


class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    id_cat = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_cat')
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'producto'


class Puntuacion(models.Model):
    id = models.IntegerField(primary_key=True)
    estrellas = models.CharField(max_length=1)
    id_viv = models.ForeignKey('Vivienda', models.DO_NOTHING, db_column='id_viv')
    id_cli = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cli')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'puntuacion'


class Recepcionista(models.Model):
    id = models.OneToOneField(Empleado, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'recepcionista'


class Registro(models.Model):
    id = models.OneToOneField(DCheck, models.DO_NOTHING, db_column='id', primary_key=True)
    id_che = models.OneToOneField(CheckIn, models.DO_NOTHING, db_column='id_che')

    class Meta:
        managed = False
        db_table = 'registro'


class Reserva(models.Model):
    id = models.IntegerField(primary_key=True)
    id_cli = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cli')
    id_viv = models.ForeignKey('Vivienda', models.DO_NOTHING, db_column='id_viv')
    fecha_reservada = models.DateField()
    estadia = models.IntegerField()
    abono = models.IntegerField()
    monto_pagado = models.IntegerField()
    total_pago = models.BigIntegerField()
    cant_adultos = models.BooleanField()
    cant_ninios = models.BooleanField(blank=True, null=True)
    cant_total = models.IntegerField()
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reserva'


class ResumenDepto(models.Model):
    id = models.IntegerField(primary_key=True)
    id_depto = models.IntegerField()
    ubicacion = models.CharField(max_length=300)
    cant_banios = models.BooleanField()
    cant_cocinas = models.BooleanField()
    cant_living = models.BooleanField()
    cant_pieza = models.BooleanField()
    cant_balcones = models.BooleanField()
    inventario = models.IntegerField()
    disponibilidad = models.CharField(max_length=10)
    id_cliente = models.CharField(max_length=100)
    nombre_cliente = models.CharField(max_length=150)
    creacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'resumen_depto'


class Sala(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sala'


class Salida(models.Model):
    id = models.OneToOneField(DCheck, models.DO_NOTHING, db_column='id', primary_key=True)
    id_che = models.OneToOneField(CheckOut, models.DO_NOTHING, db_column='id_che')

    class Meta:
        managed = False
        db_table = 'salida'


class Servicio(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    id_tip = models.ForeignKey('TipoServicio', models.DO_NOTHING, db_column='id_tip')
    id_dis = models.ForeignKey(Disponibilidad, models.DO_NOTHING, db_column='id_dis')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'servicio'


class SubCategoria(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sub_categoria'


class Sucursal(models.Model):
    id = models.IntegerField(primary_key=True)
    calle = models.CharField(max_length=20)
    num_calle = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    id_ciu = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciu')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sucursal'


class TipoDocumento(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tipo_documento'


class TipoMulta(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tipo_multa'


class TipoServicio(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tipo_servicio'


class TipoVivienda(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tipo_vivienda'


class Tour(models.Model):
    id = models.OneToOneField(Movilizacion, models.DO_NOTHING, db_column='id', primary_key=True)
    fecha_inicio = models.DateField()
    hora_inicio = models.CharField(max_length=5)
    fecha_termino = models.DateField()
    hora_termino = models.CharField(max_length=5)
    duracion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tour'


class TramoAbono(models.Model):
    id = models.IntegerField(primary_key=True)
    monto_inf = models.IntegerField()
    monto_sup = models.IntegerField()
    porcentaje = models.IntegerField()
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tramo_abono'


class TramoMulta(models.Model):
    id = models.IntegerField(primary_key=True)
    estado_prod = models.BooleanField()
    porcentaje = models.IntegerField()
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tramo_multa'


class Transporte(models.Model):
    id = models.OneToOneField(Movilizacion, models.DO_NOTHING, db_column='id', primary_key=True)
    fecha_inicio = models.DateField()
    hora_inicio = models.CharField(max_length=5)
    fecha_termino = models.DateField()
    hora_termino = models.CharField(max_length=5)
    duracion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'transporte'


class Vehiculo(models.Model):
    id = models.IntegerField(primary_key=True)
    id_mod = models.ForeignKey(Modelo, models.DO_NOTHING, db_column='id_mod')
    id_mar = models.ForeignKey(Marca, models.DO_NOTHING, db_column='id_mar')
    id_col = models.ForeignKey(Color, models.DO_NOTHING, db_column='id_col')
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vehiculo'


class Vivienda(models.Model):
    id = models.IntegerField(primary_key=True)
    latitud = models.CharField(max_length=100)
    longitud = models.CharField(max_length=100)
    estrellas = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    id_dis = models.ForeignKey(Disponibilidad, models.DO_NOTHING, db_column='id_dis')
    valor_noche = models.IntegerField()
    abono_base = models.IntegerField()
    id_ciu = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciu')
    capacidad = models.IntegerField()
    internet = models.CharField(max_length=1)
    estado = models.CharField(max_length=20)
    agua = models.CharField(max_length=1)
    luz = models.CharField(max_length=1)
    gas = models.CharField(max_length=1)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()
    id_tip = models.ForeignKey(TipoVivienda, models.DO_NOTHING, db_column='id_tip')

    class Meta:
        managed = False
        db_table = 'vivienda'
