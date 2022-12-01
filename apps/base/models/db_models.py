# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from apps.base.models.base_model import BaseModel


# business, people, users

class Acompaniante(models.Model):
    id = models.OneToOneField('people.Persona', models.DO_NOTHING, db_column='id', primary_key=True)
    class Meta:
        app_label = 'people'
        managed = True
        db_table = 'acompaniante'
        verbose_name = "Acompañante"
        verbose_name_plural = "Acompañantes"
        ordering = ['id']

    def __str__(self):
        return 'ID : ' + str(self.id)


class Cargo(BaseModel):
    descripcion = models.CharField(max_length=100, null = False, blank = False)

    class Meta:
        managed = True
        db_table = 'cargo'
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
        ordering = ['id']

    def __str__(self) -> str:
        return self.descripcion
class Categoria(BaseModel):
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    class Meta:
        managed = True
        db_table = 'categoria'
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['id']

    def __str__(self) -> str:
        return self.descripcion

class CheckIn(BaseModel):
    fecha_llegada = models.DateField(null=False, blank=False)
    hora_llegada = models.CharField(max_length=5, null=False, blank=False)
    firma = models.CharField(max_length=1, null= True)
    estado_checkin = models.CharField(max_length=30, null=False, blank=False)
    id_res = models.OneToOneField('business.Reserva', models.DO_NOTHING, db_column='id_res')
    id_rec = models.ForeignKey('people.Recepcionista', models.DO_NOTHING, db_column='id_rec')

    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'check_in'
        verbose_name = "Check In"
        verbose_name_plural = "Check In"
        ordering = ['id']

    def __str__(self) -> str:
        return 'ID : ' + str(self.id)
class CheckOut(BaseModel):
    fecha_salida = models.DateField(null=False, blank=False)
    hora_salida = models.CharField(max_length=5, blank=False, null=False)
    estado_checkout = models.CharField(max_length=30, null=False, blank=False)
    total_multa = models.IntegerField(blank=True, null=True)
    id_rec = models.ForeignKey('people.Recepcionista', models.DO_NOTHING, db_column='id_rec')
    id_res = models.OneToOneField('business.Reserva', models.DO_NOTHING, db_column='id_res')

    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'check_out'
        verbose_name = "Check Out"
        verbose_name_plural = "Check Out"
        ordering = ['id']

    def __str__(self) -> str:
        return 'ID : ' + str(self.id)
class CliAcom(BaseModel):
    app_label = 'people'
    id_res = models.ForeignKey('business.Reserva', models.DO_NOTHING, db_column='id_res')
    id_aco = models.ForeignKey(Acompaniante, models.DO_NOTHING, db_column='id_aco')
    id_cli = models.ForeignKey('people.Cliente', models.DO_NOTHING, db_column='id_cli')
    class Meta:
        managed = True
        db_table = 'cli_acom'
        verbose_name = "Detalle de Acompañante"
        verbose_name_plural = "Detalles de Acompañantes"
        ordering = ['id']


class CliCom(BaseModel):
    id_cli = models.ForeignKey('people.Cliente', models.DO_NOTHING, db_column='id_cli')
    id_viv = models.ForeignKey('business.Vivienda', models.DO_NOTHING, db_column='id_viv')
    class Meta:
        app_label = 'users'
        managed = True
        verbose_name = "Detalle comentario"
        verbose_name_plural = "Detalle de comentarios"
        ordering = ['id']
        db_table = 'cli_com'


class Cliente(models.Model):
    id = models.OneToOneField('Persona', models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        app_label = 'people'
        managed = True
        db_table = 'cliente'
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['id']

    def __str__(self) -> str:
        return 'ID : ' + str(self.id)


class Color(BaseModel):
    nombre = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'color'
        verbose_name = "Color"
        verbose_name_plural = "Colores"
        ordering = ['id']

    def __str__(self) -> str:
        return self.nombre

class Comentario(BaseModel):
    app_label = 'users'
    descripcion = models.CharField(max_length=200, null=False, blank=False)
    id_cli = models.OneToOneField('users.CliCom', models.DO_NOTHING, db_column='id_cli')

    class Meta:
        managed = True
        db_table = 'comentario'
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ['id']

    def __str__(self) -> str:
        return 'ID : ' + str(self.id) + 'ID_CLIENTE : ' + str(self.id_cli)  


class Marca(BaseModel):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    class Meta:
        managed = True
        db_table = 'marca'
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ['id']

    def __str__(self) -> str:
        return 'ID : ' + str(self.id)

class Modelo(BaseModel):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    class Meta:
        managed = True
        db_table = 'modelo'
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"
        ordering = ['id']

    def __str__(self) -> str:
        return self.nombre

class Vehiculo(BaseModel):
    patente = models.CharField(max_length=20, null=False, blank=False, unique=True)
    id_mod = models.ForeignKey(Modelo, models.DO_NOTHING, db_column='id_mod')
    id_mar = models.ForeignKey(Marca, models.DO_NOTHING, db_column='id_mar')
    id_col = models.ForeignKey(Color, models.DO_NOTHING, db_column='id_col')
    imagen = models.ImageField(upload_to='vehicle/')
    capacidad = models.IntegerField()
    class Meta:
        managed = True
        db_table = 'vehiculo'
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"
        ordering = ['id']

    def __str__(self) -> str:
        return 'ID : ' + str(self.id)

class Conductor(models.Model):
    id = models.OneToOneField('people.Empleado', models.DO_NOTHING, db_column='id', primary_key=True)
    id_veh = models.OneToOneField('base.Vehiculo', models.DO_NOTHING, db_column='id_veh')

    class Meta:
        app_label = 'people'
        managed = True
        db_table = 'conductor'
        verbose_name = "Conductor"
        verbose_name_plural = "Conductores"
        ordering = ['id']

    def __str__(self) -> str:
        return 'ID : ' + str(self.id)

class DCheck(models.Model):
    id = models.OneToOneField('business.Documento', models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'd_check'
        verbose_name = "Documento de Check"
        verbose_name_plural = "Documentos de Check"
        ordering = ['id']


class DCoordinacion(models.Model):
    id = models.OneToOneField('business.Documento', models.DO_NOTHING, db_column='id', primary_key=True)
    id_mov = models.OneToOneField('business.Movilizacion', models.DO_NOTHING, db_column='id_mov')

    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'd_coordinacion'
        verbose_name = "Documento de Coodinación"
        verbose_name_plural = "Documentos de Coodinación"
        ordering = ['id']

class DatabaseDdl(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=100)
    objeto = models.CharField(max_length=100)
    nom_objeto = models.CharField(max_length=100)
    operacion = models.CharField(max_length=100)
    creacion = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'database_ddl'


class Destino(BaseModel):
    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='travels/')
    id_ciu = models.IntegerField()
    id_est = models.IntegerField()
    id_pai = models.IntegerField()

    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'destino'


class DetServMov(BaseModel):
    id_con = models.ForeignKey('people.Conductor', models.DO_NOTHING, db_column='id_con')
    id_mov = models.ForeignKey('business.Movilizacion', models.DO_NOTHING, db_column='id_mov')
    fecha_inicio = models.DateField(null=False, blank=False)
    hora_inicio = models.CharField(max_length=5, null=False, blank=False)
    fecha_termino = models.DateField(null=False, blank=False)
    hora_termino = models.CharField(max_length=5, null=False, blank=False)
    cant_pasajeros = models.IntegerField()
    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'det_serv_mov'
        verbose_name = "Detalles de servicio de Movilización"
        verbose_name_plural = "Detalle de servicios de Movilización"
        ordering = ['id']
class DetalleMulta(BaseModel):
    id_mul = models.ForeignKey('Multa', models.DO_NOTHING, db_column='id_mul')
    id_che = models.ForeignKey(CheckOut, models.DO_NOTHING, db_column='id_che')

    class Meta:
        managed = True
        db_table = 'detalle_multa'
        verbose_name = "Detalle de multa"
        verbose_name_plural = "Detalles de multas"
        ordering = ['id']

class DetalleProducto(BaseModel):
    id_est = models.ForeignKey('business.EstadoProducto', models.DO_NOTHING, db_column='id_est')
    id_det = models.ForeignKey('business.DetalleSala', models.DO_NOTHING, db_column='id_det')
    id_pro = models.ForeignKey('business.Producto', models.DO_NOTHING, db_column='id_pro')

    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'detalle_producto'
        verbose_name = "Detalle de producto"
        verbose_name_plural = "Detalles de productos"
        ordering = ['id']


class DetalleSala(BaseModel):
    id_inv = models.ForeignKey('business.Inventario', models.DO_NOTHING, db_column='id_inv')
    id_sal = models.ForeignKey('business.Sala', models.DO_NOTHING, db_column='id_sal')
    imagen_sala = models.ImageField(upload_to='rooms/')

    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'detalle_sala'
        verbose_name = "Detalle de sala"
        verbose_name_plural = "Detalles de salas"
        ordering = ['id']


#class DetalleServicio(BaseModel):
#    id_res = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='id_res')
#    id_ser = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_ser')

#    class Meta:
#        managed = True
#        db_table = 'detalle_servicio'


class DetalleTour(BaseModel):
    id_tou = models.ForeignKey('business.Tour', models.DO_NOTHING, db_column='id_tou')
    id_des = models.ForeignKey('business.Destino', models.DO_NOTHING, db_column='id_des')

    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'detalle_tour'
        verbose_name = "Detalle de Tour"
        verbose_name_plural = "Detalles de Tours"
        ordering = ['id']


class Disponibilidad(BaseModel):
    app_label = 'business'
    descripcion = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'disponibilidad'
        verbose_name = "Disponibilidad"
        verbose_name_plural = "Disponibilidades"
        ordering = ['id']

    def __str__(self) -> str:
        return self.descripcion

class DocIdentidad(BaseModel):
    descripcion = models.CharField(max_length=80, null=False, blank=False)
    class Meta:
        app_label = 'people'
        managed = True
        db_table = 'doc_identidad'
        verbose_name = "Documento de Identidad"
        verbose_name_plural = "Documentos de Identidad"
        ordering = ['id']

    def __str__(self) -> str:
        return self.descripcion
class Documento(BaseModel):
    id_tip = models.ForeignKey('TipoDocumento', models.DO_NOTHING, db_column='id_tip')

    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'documento'
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
        ordering = ['id']

    def __str__(self) -> str:
        return 'ID : ' + str(self.id)

class Empleado(models.Model):
    id = models.OneToOneField('people.Persona', models.DO_NOTHING, db_column='id', primary_key=True)
    sueldo = models.IntegerField()
    fecha_contrato = models.DateField()
    id_car = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='id_car')

    class Meta:
        app_label = 'people'
        managed = True
        db_table = 'empleado'
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ['id']

    def __str__(self) -> str:
        return 'ID : ' + str(self.id)

class ErrorProceso(models.Model):
    id = models.IntegerField(primary_key=True)
    cod_error = models.CharField(max_length=100)
    subprograma = models.CharField(max_length=100)
    mensaje_error = models.CharField(max_length=300)
    creacion = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'error_proceso'


class EstadoCivil(BaseModel):
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    class Meta:
        managed = True
        db_table = 'estado_civil'
        verbose_name = "Estado Civil"
        verbose_name_plural = "Estados Civiles"
        ordering = ['id']

    def __str__(self) -> str:
        return self.descripcion

class EstadoProducto(BaseModel):
    descripcion = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'estado_producto'


class GaleriaExterior(BaseModel):
    app_label = 'business'
    imagen = models.ImageField(upload_to='exterior_gallery/')
    id_viv = models.ForeignKey('business.Vivienda', models.DO_NOTHING, db_column='id_viv')
    class Meta:
        managed = True
        db_table = 'galeria_exterior'
        verbose_name = "Galería De Exterior"
        verbose_name_plural = "Galerías De Exteriores"
        ordering = ['id']

    def __str__(self) -> str:
        return 'ID_VIVIENDA : ' + str(self.id_viv)

class GaleriaInterior(BaseModel):
    app_label = 'business'
    imagen = models.ImageField(upload_to='interior_gallery/')
    id_viv = models.ForeignKey('business.Vivienda', models.DO_NOTHING, db_column='id_viv')

    class Meta:
        managed = True
        db_table = 'galeria_interior'
        verbose_name = "Galería De Interior"
        verbose_name_plural = "Galerías De Interiores"
        ordering = ['id']

    def __str__(self) -> str:
        return 'ID_VIVIENDA : ' + str(self.id_viv)

class Genero(BaseModel):
    descripcion = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        app_label = 'people'
        managed = True
        db_table = 'genero'
        verbose_name = "Genero"
        verbose_name_plural = "Generos"
        ordering = ['id']

    def __str__(self) -> str:
        return self.descripcion

class Inventario(BaseModel):
    id_viv = models.OneToOneField('business.Vivienda', models.DO_NOTHING, db_column='id_viv')
    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'inventario'
        verbose_name = "Inventario"
        verbose_name_plural = "Inventarios"
        ordering = ['id']

class Movilizacion(models.Model):
    id = models.OneToOneField('business.Servicio', models.DO_NOTHING, db_column='id', primary_key=True)
    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'movilizacion'
        verbose_name = "Servicio de Movilización"
        verbose_name_plural = "Servicios de Movilización"
        ordering = ['id']

class Multa(BaseModel):
    app_label = 'business'
    descripcion = models.CharField(max_length=200)
    monto = models.IntegerField()
    id_tip = models.ForeignKey('business.TipoMulta', models.DO_NOTHING, db_column='id_tip')

    class Meta:
        managed = True
        db_table = 'multa'
        verbose_name = "Multa"
        verbose_name_plural = "Multas"
        ordering = ['id']

    def __str__(self) -> str:
        return 'ID : ' + str(self.id)


class Persona(BaseModel):
    run = models.CharField(unique=True, max_length=15, blank=True, null=True)
    dv = models.CharField(max_length=1, blank=True, null=True)
    pasaporte = models.CharField(unique=True, max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    snombre = models.CharField(max_length=50, blank=True, null=True)
    ap_paterno = models.CharField(max_length=50, null=False, blank=False)
    ap_materno = models.CharField(max_length=50, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    telefono = models.CharField(max_length=20, null=False, blank=False)
    num_calle = models.CharField(max_length=10,null=False, blank=False)
    calle = models.CharField(max_length=30, null=False, blank=False)
    id_ciu = models.IntegerField()
    id_est = models.IntegerField()
    id_pai = models.IntegerField()
    id_doc = models.ForeignKey(DocIdentidad, models.DO_NOTHING, db_column='id_doc')
    id_est1 = models.ForeignKey(EstadoCivil, models.DO_NOTHING, db_column='id_est1')
    id_gen = models.ForeignKey('people.Genero', models.DO_NOTHING, db_column='id_gen')

    class Meta:
        app_label = 'people'
        managed = True
        db_table = 'persona'
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering = ['id']

    def __str__(self) -> str:
        return 'ID : ' + str(self.id) + ' ' + self.nombre + ' ' + self.ap_paterno



class Producto(BaseModel):
    id_cat = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_cat')
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)
    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'producto'
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['id']

    def __str__(self) -> str:
        return self.descripcion

class Puntuacion(BaseModel):
    estrellas = models.CharField(max_length=1, null=False, blank=False)
    id_viv = models.ForeignKey('business.Vivienda', models.DO_NOTHING, db_column='id_viv')
    id_cli = models.ForeignKey('people.Cliente', models.DO_NOTHING, db_column='id_cli')

    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'puntuacion'
        verbose_name = "Puntuación"
        verbose_name_plural = "Puntuaciones"
        ordering = ['id']

    def __str__(self) -> str:
        return 'ID : ' + str(self.id)

class Recepcionista(models.Model):
    id = models.OneToOneField('people.Empleado', models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        app_label = 'people'
        managed = True
        db_table = 'recepcionista'
        verbose_name = "Recepcionista"
        verbose_name_plural = "Recepcionistas"
        ordering = ['id']

    def __str__(self) -> str:
        return 'ID : ' + str(self.id)
    
class Registro(models.Model):
    id = models.OneToOneField('business.DCheck', models.DO_NOTHING, db_column='id', primary_key=True)
    id_che = models.OneToOneField('business.CheckIn', models.DO_NOTHING, db_column='id_che')

    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'registro'
        verbose_name = "Documento de Check-in"
        verbose_name_plural = "Documentos de Check-in"
        ordering = ['id']

class Reserva(BaseModel):
    id_cli = models.ForeignKey('people.Cliente', models.DO_NOTHING, db_column='id_cli')
    id_viv = models.ForeignKey('business.Vivienda', models.DO_NOTHING, db_column='id_viv')
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_termino = models.DateField(null=False, blank=False)
    abono = models.IntegerField(null=False, blank=False)
    monto_pagado = models.IntegerField(null=False, blank=False)
    total_pago = models.BigIntegerField(null=False,blank=False)
    cant_acompaniante = models.IntegerField()
    cant_total = models.IntegerField()

    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'reserva'
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ['id']

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
        managed = True
        db_table = 'resumen_depto'


class Sala(BaseModel):
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'sala'
        verbose_name = "Sala"
        verbose_name_plural = "Salas"
        ordering = ['id']

    def __str__(self) -> str:
        return self.descripcion

class Salida(models.Model):
    id = models.OneToOneField('business.DCheck', models.DO_NOTHING, db_column='id', primary_key=True)
    id_che = models.OneToOneField('business.CheckOut', models.DO_NOTHING, db_column='id_che')

    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'salida'
        verbose_name = "Documento de Check-out"
        verbose_name_plural = "Documentos de Check-out"
        ordering = ['id']

class Sucursal(BaseModel):
    calle = models.CharField(max_length=20)
    num_calle = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    id_pai = models.IntegerField()
    id_est = models.IntegerField()
    id_ciu = models.IntegerField()
    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'sucursal'

class TipoDocumento(BaseModel):
    descripcion = models.CharField(max_length=50, null=False, blank=False)
    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'tipo_documento'
        verbose_name = "Tipo de documento"
        verbose_name_plural = "Tipos de documentos"
        ordering = ['id']

    def __str__(self):
        return 'Tipo Documento ' + self.descripcion


class TipoMulta(BaseModel):
    descripcion = models.CharField(max_length=100, null=False, blank=True)
    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'tipo_multa'
        verbose_name = "Tipo de Multa"
        verbose_name_plural = "Tipos de Multa"
        ordering = ['id']

    def __str__(self):
        return 'Tipo Multa ' + self.descripcion

class TipoServicio(BaseModel):
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'tipo_servicio'
        verbose_name = "Tipo de servicio"
        verbose_name_plural = "Tipos de servicios"
        ordering = ['id']

class TipoVivienda(BaseModel):
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    class Meta:
        app_label = 'business' 
        managed = True
        db_table = 'tipo_vivienda'
        verbose_name = "Tipo Vivienda"
        verbose_name_plural = "Tipos de Vivienda"
        ordering = ['id']

    def __str__(self) -> str:
        return 'ID : ' + str(self.id)

class Tour(models.Model):
    id = models.OneToOneField('business.Movilizacion', models.DO_NOTHING, db_column='id', primary_key=True)
    id_ub_trans = models.ForeignKey('business.UbicacionTrans', models.DO_NOTHING, db_column='id_ub_trans')
    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'tour'
        verbose_name = "Servicio de Tour"
        verbose_name_plural = "Servicios de Tours"
        ordering = ['id']

class TramoAbono(models.Model):
    id = models.IntegerField(primary_key=True)
    monto_inf = models.IntegerField()
    monto_sup = models.IntegerField()
    porcentaje = models.IntegerField()
    estado = models.CharField(max_length=15)
    creacion = models.DateTimeField()
    actualizacion = models.DateTimeField()

    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'tramo_abono'


class TramoMulta(BaseModel):
    estado_prod = models.IntegerField()
    porcentaje = models.IntegerField()

    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'tramo_multa'
        verbose_name = "Tramo de multa"
        verbose_name_plural = "Tramos de multas"
        ordering = ['id']
class Transporte(models.Model):
    id = models.OneToOneField('business.Movilizacion', models.DO_NOTHING, db_column='id', primary_key=True)
    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'transporte'
        verbose_name = "Servicio de transporte"
        verbose_name_plural = "Servicios de transporte"
        ordering = ['id']

class TransporteIda(BaseModel):
    id_trans = models.OneToOneField('business.Transporte', models.DO_NOTHING, db_column='id_trans')
    id_ub_trans = models.ForeignKey('business.UbicacionTrans', models.DO_NOTHING, db_column='id_ub_trans')

    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'transporte_ida'
        verbose_name = "Servicio de transporte de ida"
        verbose_name_plural = "Servicios de transportes de ida"
        ordering = ['id']
class TransporteVuelta(BaseModel):
    id_trans = models.OneToOneField('business.Transporte', models.DO_NOTHING, db_column='id_trans')
    id_ub_trans = models.ForeignKey('business.UbicacionTrans', models.DO_NOTHING, db_column='id_ub_trans')

    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'transporte_vuelta'
        verbose_name = "Servicio de transporte de vuelta"
        verbose_name_plural = "Servicios de transportes de vuelta"
        ordering = ['id']
class TipoUbicacion(BaseModel):
    descripcion = models.CharField(max_length = 200, null=False, blank=False)
    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'tipo_ubicacion'
        verbose_name = "Tipo de ubicación"
        verbose_name_plural = "Tipos de ubicaciones"
        ordering = ['id']
class UbicacionTrans(BaseModel):
    id_tip = models.ForeignKey('business.TipoUbicacion', models.DO_NOTHING, db_column='id_tip')
    id_ciu = models.IntegerField()
    nombre = models.CharField(max_length = 100, null=False, blank=False)
    categoria = models.CharField(max_length = 100, null=False, blank=False) 
    descripcion = models.CharField(max_length = 200, null=True, blank=True)
    imagen = models.ImageField(upload_to='tr_location/', null=True)
    precio = models.IntegerField(null=False, blank=False)
    latitud = models.CharField(max_length = 100)
    longitud = models.CharField(max_length = 100)

    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'ubicacion_trans'
        verbose_name = "Ubicación de transporte"
        verbose_name_plural = "Ubicaciones de transporte"
        ordering = ['id']
class Vivienda(BaseModel):
    latitud = models.CharField(max_length=100, null=False, blank=False)
    longitud = models.CharField(max_length=100, null=False, blank=False)
    m2 = models.CharField(max_length=30, null=False, blank=False)
    estrellas = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    id_dis = models.ForeignKey(Disponibilidad, models.DO_NOTHING, db_column='id_dis')
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    slug = models.CharField(max_length=30, null=False, blank=False)
    imagen_principal = models.ImageField(upload_to='viviendas/')
    valor_noche = models.IntegerField(null=False, blank=False)
    abono_base = models.IntegerField(null=False, blank=False)
    id_pai = models.IntegerField(null=False, blank=False)
    id_est = models.IntegerField(null=False, blank=False)
    id_ciu = models.IntegerField(null=False, blank=False)
    capacidad = models.IntegerField(null=False, blank=False)
    internet = models.CharField(max_length=1, null=False, blank=False)
    agua = models.CharField(max_length=1, null=False, blank=False)
    luz = models.CharField(max_length=1, null=False, blank=False)
    gas = models.CharField(max_length=1, null=False, blank=False)
    id_tip = models.ForeignKey(TipoVivienda, models.DO_NOTHING, db_column='id_tip')

    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'vivienda'
        verbose_name = "Vivienda"
        verbose_name_plural = "Viviendas"
        ordering = ['id']

    def __str__(self) -> str:
        return 'ID : ' + str(self.id)


class Compra(BaseModel):
    id_reserva = models.OneToOneField('business.Reserva', models.DO_NOTHING, db_column='id_reserva')
    id_cliente = models.ForeignKey('people.Cliente', models.DO_NOTHING, db_column='id_cliente')
    monto_final = models.IntegerField()
    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'compra'
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        ordering = ['id']
class Servicio(BaseModel):
    precio = models.IntegerField(null=False, blank=False)
    id_tip = models.ForeignKey('business.TipoServicio', models.DO_NOTHING, db_column='id_tip')
    id_reserva = models.ForeignKey('business.Reserva', models.DO_NOTHING, db_column='id_reserva')
    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'servicio'
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['id']

    def to_dict(self):
        return {
            'id': self.id,
            'precio': self.precio,
            'id_reserva': self.id_reserva.id,
            'id_tip' : self.id_tip.id
        }

class DetProyecto(BaseModel):
    id_viv = models.ForeignKey('business.Vivienda', models.DO_NOTHING, db_column='id_viv')
    id_emp = models.ForeignKey('people.Empleado', models.DO_NOTHING, db_column='id_emp')
    class Meta:
        app_label = 'business'
        managed = True
        db_table = 'det_proyecto'
        verbose_name = "Detalle del proyecto"
        verbose_name_plural = "Detalles del proyecto"
        ordering = ['id']