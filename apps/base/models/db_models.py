# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from apps.base.models.base_model import BaseModel


class Acompaniante(models.Model):
    id = models.OneToOneField('Persona', models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'acompaniante'


class Cargo(BaseModel):
    descripcion = models.CharField(max_length=100)


    class Meta:
        managed = False
        db_table = 'cargo'


class Categoria(BaseModel):
    descripcion = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'categoria'


class CheckIn(BaseModel):
    fecha_llegada = models.DateField()
    hora_llegada = models.CharField(max_length=5)
    firma = models.CharField(max_length=1)
    id_res = models.OneToOneField('Reserva', models.DO_NOTHING, db_column='id_res')
    id_rec = models.ForeignKey('Recepcionista', models.DO_NOTHING, db_column='id_rec')

    class Meta:
        managed = False
        db_table = 'check_in'


class CheckOut(BaseModel):
    fecha_salida = models.DateField()
    hora_salida = models.CharField(max_length=5, blank=True, null=True)
    total_multa = models.IntegerField(blank=True, null=True)
    id_rec = models.ForeignKey('Recepcionista', models.DO_NOTHING, db_column='id_rec')
    id_res = models.OneToOneField('Reserva', models.DO_NOTHING, db_column='id_res')

    class Meta:
        managed = False
        db_table = 'check_out'


# No se puede heredar debido a que no usa secuencia autoincrementable
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


class CliAcom(BaseModel):
    id_res = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='id_res')
    id_aco = models.ForeignKey(Acompaniante, models.DO_NOTHING, db_column='id_aco')
    id_cli = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cli')
    class Meta:
        managed = False
        db_table = 'cli_acom'


class CliCom(BaseModel):
    id_cli = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cli')
    id_viv = models.ForeignKey('Vivienda', models.DO_NOTHING, db_column='id_viv')
    class Meta:
        managed = False
        db_table = 'cli_com'


class Cliente(models.Model):
    id = models.OneToOneField('Persona', models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Color(BaseModel):
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'color'

class Comentario(BaseModel):
    descripcion = models.CharField(max_length=200)
    id_cli = models.OneToOneField(CliCom, models.DO_NOTHING, db_column='id_cli')

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


class Destino(BaseModel):
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'destino'


class DetServMov(BaseModel):
    id_con = models.ForeignKey(Conductor, models.DO_NOTHING, db_column='id_con')
    id_mov = models.ForeignKey('Movilizacion', models.DO_NOTHING, db_column='id_mov')

    class Meta:
        managed = False
        db_table = 'det_serv_mov'


class DetVehMov(BaseModel):
    id_veh = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='id_veh')
    id_mov = models.ForeignKey('Movilizacion', models.DO_NOTHING, db_column='id_mov')

    class Meta:
        managed = False
        db_table = 'det_veh_mov'


class DetalleMulta(BaseModel):
    id_mul = models.ForeignKey('Multa', models.DO_NOTHING, db_column='id_mul')
    id_che = models.ForeignKey(CheckOut, models.DO_NOTHING, db_column='id_che')

    class Meta:
        managed = False
        db_table = 'detalle_multa'


class DetalleProducto(BaseModel):
    id_est = models.ForeignKey('EstadoProducto', models.DO_NOTHING, db_column='id_est')
    id_det = models.ForeignKey('DetalleSala', models.DO_NOTHING, db_column='id_det')
    id_pro = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_pro')

    class Meta:
        managed = False
        db_table = 'detalle_producto'


class DetalleSala(BaseModel):
    id_inv = models.ForeignKey('Inventario', models.DO_NOTHING, db_column='id_inv')
    id_sal = models.ForeignKey('Sala', models.DO_NOTHING, db_column='id_sal')
    imagen_sala = models.TextField()

    class Meta:
        managed = False
        db_table = 'detalle_sala'


class DetalleServicio(BaseModel):
    id_res = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='id_res')
    id_ser = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_ser')

    class Meta:
        managed = False
        db_table = 'detalle_servicio'


class DetalleTour(BaseModel):
    id_tou = models.ForeignKey('Tour', models.DO_NOTHING, db_column='id_tou')
    id_des = models.ForeignKey(Destino, models.DO_NOTHING, db_column='id_des')

    class Meta:
        managed = False
        db_table = 'detalle_tour'


class Disponibilidad(BaseModel):
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'disponibilidad'


class DocIdentidad(BaseModel):
    descripcion = models.CharField(max_length=80)
    class Meta:
        managed = False
        db_table = 'doc_identidad'

class Documento(BaseModel):
    id_tip = models.ForeignKey('TipoDocumento', models.DO_NOTHING, db_column='id_tip')

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


class EstadoCivil(BaseModel):
    descripcion = models.CharField(max_length=100)
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


class EstadoProducto(BaseModel):
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_producto'


class GaleriaExterior(BaseModel):
    imagen = models.TextField()
    id_viv = models.ForeignKey('Vivienda', models.DO_NOTHING, db_column='id_viv')
    class Meta:
        managed = False
        db_table = 'galeria_exterior'


class GaleriaInterior(BaseModel):
    imagen = models.TextField()
    id_viv = models.ForeignKey('Vivienda', models.DO_NOTHING, db_column='id_viv')

    class Meta:
        managed = False
        db_table = 'galeria_interior'


class Genero(BaseModel):
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'genero'


class Inventario(BaseModel):
    id_viv = models.OneToOneField('Vivienda', models.DO_NOTHING, db_column='id_viv')
    class Meta:
        managed = False
        db_table = 'inventario'


class Marca(BaseModel):
    nombre = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'marca'


class Modelo(BaseModel):
    nombre = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'modelo'


class Movilizacion(models.Model):
    id = models.OneToOneField('Servicio', models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'movilizacion'


class Multa(BaseModel):
    descripcion = models.CharField(max_length=200)
    monto = models.IntegerField()
    id_tip = models.ForeignKey('TipoMulta', models.DO_NOTHING, db_column='id_tip')

    class Meta:
        managed = False
        db_table = 'multa'


class Pais(models.Model):
    id = models.IntegerField(primary_key=True)
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


class Persona(BaseModel):
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
    id_ciu = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciu')
    id_est = models.ForeignKey(EstadoPais, models.DO_NOTHING, db_column='id_est')
    id_pai = models.ForeignKey(Pais, models.DO_NOTHING, db_column='id_pai')
    id_doc = models.ForeignKey(DocIdentidad, models.DO_NOTHING, db_column='id_doc')
    id_est1 = models.ForeignKey(EstadoCivil, models.DO_NOTHING, db_column='id_est1')
    id_gen = models.ForeignKey(Genero, models.DO_NOTHING, db_column='id_gen')

    class Meta:
        managed = False
        db_table = 'persona'


class Producto(BaseModel):
    id_cat = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_cat')
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'producto'


class Puntuacion(BaseModel):
    estrellas = models.CharField(max_length=1)
    id_viv = models.ForeignKey('Vivienda', models.DO_NOTHING, db_column='id_viv')
    id_cli = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cli')

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


class Reserva(BaseModel):
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


class Sala(BaseModel):
    descripcion = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'sala'


class Salida(models.Model):
    id = models.OneToOneField(DCheck, models.DO_NOTHING, db_column='id', primary_key=True)
    id_che = models.OneToOneField(CheckOut, models.DO_NOTHING, db_column='id_che')

    class Meta:
        managed = False
        db_table = 'salida'


class Servicio(BaseModel):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    id_tip = models.ForeignKey('TipoServicio', models.DO_NOTHING, db_column='id_tip')
    id_dis = models.ForeignKey(Disponibilidad, models.DO_NOTHING, db_column='id_dis')
    class Meta:
        managed = False
        db_table = 'servicio'


class Sucursal(BaseModel):
    calle = models.CharField(max_length=20)
    num_calle = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    id_ciu = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciu')
    class Meta:
        managed = False
        db_table = 'sucursal'

class TipoDocumento(BaseModel):
    descripcion = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'tipo_documento'


class TipoMulta(BaseModel):
    descripcion = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'tipo_multa'


class TipoServicio(BaseModel):
    descripcion = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'tipo_servicio'


class TipoVivienda(BaseModel):
    descripcion = models.CharField(max_length=100)
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


class Vehiculo(BaseModel):
    id_mod = models.ForeignKey(Modelo, models.DO_NOTHING, db_column='id_mod')
    id_mar = models.ForeignKey(Marca, models.DO_NOTHING, db_column='id_mar')
    id_col = models.ForeignKey(Color, models.DO_NOTHING, db_column='id_col')
    class Meta:
        managed = False
        db_table = 'vehiculo'


class Vivienda(BaseModel):
    latitud = models.CharField(max_length=100)
    longitud = models.CharField(max_length=100)
    m2 = models.CharField(max_length=30)
    estrellas = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    id_dis = models.ForeignKey(Disponibilidad, models.DO_NOTHING, db_column='id_dis')
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    slug = models.CharField(max_length=30)
    imagen_principal = models.TextField()
    valor_noche = models.IntegerField()
    abono_base = models.IntegerField()
    id_ciu = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciu')
    capacidad = models.IntegerField()
    internet = models.CharField(max_length=1)
    agua = models.CharField(max_length=1)
    luz = models.CharField(max_length=1)
    gas = models.CharField(max_length=1)
    id_tip = models.ForeignKey(TipoVivienda, models.DO_NOTHING, db_column='id_tip')

    class Meta:
        managed = False
        db_table = 'vivienda'
