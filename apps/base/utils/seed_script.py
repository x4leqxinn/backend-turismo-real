from apps.base.models.db_models import *
from apps.users.models import User, UserRole
from django.contrib.auth.models import Group
from django.db import connections

GRUPOS : list[Group] = [
    Group(name = 'Administrador'),
    Group(name = 'Empleado'),
    Group(name = 'Cliente'),
]

ROLES : list[UserRole] = [
    UserRole(description = 'Administrador'),
    UserRole(description = 'Empleado'),
    UserRole(description = 'Cliente'),
]

CARGOS : list[Cargo] = [
    Cargo(descripcion = 'Administrador web'),
    Cargo(descripcion = 'Administrador de base de datos'),
    Cargo(descripcion = 'Recepcionista'),
    Cargo(descripcion = 'Conductor')
]

CATEGORIAS : list[Categoria] = [
    Categoria(descripcion = 'Mobiliario'),
    Categoria(descripcion = 'Electrodoméstico'),
    Categoria(descripcion = 'Belleza')
]

DISPONIBILIDADES : list[Disponibilidad] = [
    Disponibilidad(descripcion = 'DISPONIBLE'),
    Disponibilidad(descripcion = 'NO DISPONIBLE')
]

COLORES : list[Color] = [
    Color(nombre = 'Negro'),
    Color(nombre = 'Blanco'),
    Color(nombre = 'Rojo'),
    Color(nombre = 'Verde'),
    Color(nombre = 'Naranja'),
    Color(nombre = 'Azul'),
]

MODELOS : list[Modelo] = [
    Modelo(nombre = 'ÑUÑUKI'),
    Modelo(nombre = 'AUDI'),
]

MARCAS : list[Marca] = [
    Marca(nombre = 'Marca de prueba 1'),
    Marca(nombre = 'Marca de prueba 2'),
]

GENEROS : list[Genero] = [
    Genero(descripcion = 'MASCULINO'),
    Genero(descripcion = 'FEMENINO'),
    Genero(descripcion = 'OTRO')
]

DOCUMENTOS_IDENTIDAD : list[DocIdentidad] = [
    DocIdentidad(descripcion = 'CÉDULA DE IDENTIDAD'),
    DocIdentidad(descripcion = 'PASAPORTE')
]

ESTADO_CIVILES : list[EstadoCivil] = [
    EstadoCivil(descripcion = 'SOLTERO/A'),
    EstadoCivil(descripcion = 'CASADO/A'),
    EstadoCivil(descripcion = 'COMPLICADO/A')
]

ESTADOS_PRODUCTOS : list[EstadoProducto] = [
    EstadoProducto(descripcion = 'PERFECTO'),
    EstadoProducto(descripcion = 'BUEN ESTADO'),
    EstadoProducto(descripcion = 'PARCIALMENTE DAÑADO'),
    EstadoProducto(descripcion = 'DAÑADO'),
    EstadoProducto(descripcion = 'MUY DAÑADO'),
    EstadoProducto(descripcion = 'INUTILIZABLE')
]

SALAS : list[Sala] = [
    Sala(descripcion = 'LIVING'),
    Sala(descripcion = 'COCINA'),
    Sala(descripcion = 'COMEDOR'),
    Sala(descripcion = 'BAÑO'),
    Sala(descripcion = 'BALCÓN'),
    Sala(descripcion = 'DORMITORIO'),
    Sala(descripcion = 'ESTACIONAMIENTO')
]

PERSONAS : list[Persona] = [
    ## ADMINISTRADORES
    Persona(run = '20281676',dv = '2', nombre = 'Jorge' , snombre = 'Alejandro' , ap_paterno = 'Quintui', ap_materno = 'Vergara', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    Persona(run = '372893',dv = '2', nombre = 'Lucas' , snombre = 'nn' , ap_paterno = 'Menares', ap_materno = 'fds', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'fsdfs', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    Persona(run = '423',dv = '2', nombre = 'Paula' , snombre = 'd' , ap_paterno = 'Soto', ap_materno = 'Retamal', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'fdsf', id_gen = GENEROS[1], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    Persona(run = '439482',dv = '2', nombre = 'Joaquín' , snombre = 'Antonio' , ap_paterno = 'Reyes', ap_materno = 'Montero', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'mona xina', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    Persona(run = '4893284',dv = '2', nombre = 'Paula' , snombre = 'a' , ap_paterno = 'Piña', ap_materno = 'Marin', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[1], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    
    ## CONDUCTORES
    Persona(run = '11111111',dv = '1', nombre = 'Matias' , snombre = 'a' , ap_paterno = 'Menares', ap_materno = 'ijd', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    Persona(run = '22222222',dv = '1', nombre = 'Alfonso' , snombre = 'a' , ap_paterno = 'Pacheco', ap_materno = 'fjklsdj', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),

    ## RECEPCIONISTAS
    #Persona(run = '22222222',dv = '1', nombre = 'Alfonso' , snombre = 'a' , ap_paterno = 'Pacheco', ap_materno = 'Marin', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    #Persona(run = '22222222',dv = '1', nombre = 'Alfonso' , snombre = 'a' , ap_paterno = 'Pacheco', ap_materno = 'Marin', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    #Persona(run = '22222222',dv = '1', nombre = 'Alfonso' , snombre = 'a' , ap_paterno = 'Pacheco', ap_materno = 'Marin', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    
    ## CLIENTES PARA TEST
    Persona(run = '87843',dv = '1', nombre = 'Exclavo' , snombre = 'a' , ap_paterno = 'Sexual', ap_materno = 'uwu', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
]

EMPLEADOS : list[Empleado] = [
    Empleado(id = PERSONAS[0], sueldo = 99999, fecha_contrato = '2022-08-01', id_car = CARGOS[1]),
    Empleado(id = PERSONAS[1], sueldo = 99999, fecha_contrato = '2022-08-01', id_car = CARGOS[1]),
    Empleado(id = PERSONAS[2], sueldo = 99999, fecha_contrato = '2022-08-01', id_car = CARGOS[1]),
    Empleado(id = PERSONAS[3], sueldo = 99999, fecha_contrato = '2022-08-01', id_car = CARGOS[1]),
    Empleado(id = PERSONAS[4], sueldo = 99999, fecha_contrato = '2022-08-01', id_car = CARGOS[1]),
    ## Conductores
    Empleado(id = PERSONAS[5], sueldo = 99999, fecha_contrato = '2022-08-01', id_car = CARGOS[3]),
    Empleado(id = PERSONAS[6], sueldo = 99999, fecha_contrato = '2022-08-01', id_car = CARGOS[3]),
]

VEHICULOS : list[Vehiculo] = [
    Vehiculo(patente = 'AO32FNV', id_mod = MODELOS[0], id_mar = MARCAS[0], id_col = COLORES[0], capacidad = 5, imagen = None),
    Vehiculo(patente = 'XDJN72', id_mod = MODELOS[1], id_mar = MARCAS[1], id_col = COLORES[1], capacidad = 5, imagen = None),
]

CONDUCTORES : list[Conductor] = [
    Conductor(id = EMPLEADOS[5], id_veh = VEHICULOS[0]),
    Conductor(id = EMPLEADOS[6], id_veh = VEHICULOS[1]),
]

CLIENTES : list[Cliente] = [
    Cliente(id = PERSONAS[7]),
]

def get_user(email : str, role : UserRole, person : Persona, password : str) -> User:
    user = User(email = email, role = role, person = person, is_staff = True, is_superuser = True)
    user.set_password(password)
    return user

USUARIOS : list[User] = [
    get_user('jorgealequinn@gmail.com',ROLES[0],PERSONAS[0],'Admin123!'),
    get_user('lucasmenaresaguirre@gmail.com',ROLES[0],PERSONAS[1],'Admin123!'),
    get_user('paulasotoretamal@gmail.com',ROLES[0],PERSONAS[2],'Admin123!'),
    get_user('joaking.twitch001@gmail.com',ROLES[0],PERSONAS[3],'Admin123!'),
    get_user('paulapinamarin@gmail.com',ROLES[0],PERSONAS[4],'Admin123!'),
    get_user('mats@gmail.com',ROLES[1],PERSONAS[5],'Admin123!'),
    get_user('alcheco@gmail.com',ROLES[1],PERSONAS[6],'Admin123!'),
]

PRODUCTOS : list[Producto] = [
    Producto(id_cat = CATEGORIAS[1],descripcion ='Televisor', precio = 999),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Cocina',precio = 99999),
    Producto(id_cat = CATEGORIAS[1],descripcion = 'Refrigerador',precio = 99999),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Ducha',precio = 99999),
    Producto(id_cat = CATEGORIAS[1],descripcion = 'Microondas',precio = 99999),
    Producto(id_cat = CATEGORIAS[1],descripcion = 'Aspiradora',precio = 99999),
    Producto(id_cat = CATEGORIAS[1],descripcion = 'Juguera',precio = 99999),
    Producto(id_cat = CATEGORIAS[1],descripcion = 'Tostador',precio = 99999),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Velador',precio = 99999),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Cómoda',precio = 99999),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Clóset',precio = 99999),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Escritorio',precio = 99999),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Armario',precio = 99999),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Estante',precio = 99999),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Sofá',precio = 99999),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Cama 2 plazas',precio = 99999),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Cama individual',precio = 99999),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Mesa ',precio = 99999),
    Producto(id_cat = CATEGORIAS[2],descripcion = 'Secador ',precio = 99999),
    Producto(id_cat = CATEGORIAS[2],descripcion = 'Depilador',precio = 99999),
    Producto(id_cat = CATEGORIAS[2],descripcion = 'Plancha alisadora',precio = 99999),
    Producto(id_cat = CATEGORIAS[2],descripcion = 'Afeitadora',precio = 99999),
    Producto(id_cat = CATEGORIAS[1],descripcion = 'Lavadora',precio = 99999)
]

TIPOS_DOCUMENTOS : list[TipoDocumento] = [
    TipoDocumento(descripcion = 'CHECK IN'),
    TipoDocumento(descripcion = 'CHECK OUT'),
    TipoDocumento(descripcion = 'CHECK COORDINACION')
]

TIPOS_VIVIENDAS : list[TipoVivienda] = [
    TipoVivienda(descripcion = 'Departamento'),
    TipoVivienda(descripcion = 'Casa'),
    TipoVivienda(descripcion = 'Parcela')
]

TIPOS_SERVICIOS : list[TipoServicio] = [
    TipoServicio(descripcion = 'TRANSPORTE'),
    TipoServicio(descripcion = 'TOUR')
]

TIPOS_UBICACIONES : list[TipoUbicacion] = [
    TipoUbicacion(descripcion = 'Terminal de buses'),
    TipoUbicacion(descripcion = 'Aeropuerto'),
]

UBICACIONES_TRANSPORTES : list[UbicacionTrans] = [
    UbicacionTrans(nombre = 'Terminal de buses san bernardo', precio = 9999, latitud = '72387', longitud = '423423', id_tip = TIPOS_UBICACIONES[0], id_ciu = 1),
    UbicacionTrans(nombre = 'Terminal de buses mona xina crew', precio = 9999, latitud = '72387', longitud = '423423', id_tip = TIPOS_UBICACIONES[0], id_ciu = 1),
]

VIVIENDAS : list[Vivienda] = [
    Vivienda(latitud = '-33.5342',longitud = '-70.59299',m2 = '53.45',estrellas = None,id_dis = DISPONIBILIDADES[0], nombre = 'Gran Avenida', descripcion = 'Departamento amplio, esta es una descripción de prueba',direccion = 'Calle Prueba #123',slug = 'gran-avenida',imagen_principal = None,valor_noche = '50000',abono_base = 0,id_ciu = '19111', id_est = '2824',id_pai = '44',capacidad = '3', id_tip = TIPOS_VIVIENDAS[0], internet = '1', luz = '1' , gas = '1', agua = '1'),
    Vivienda(latitud = '-33.5342',longitud = '-70.59299',m2 = '23.45',estrellas = None,id_dis = DISPONIBILIDADES[0], nombre = 'Hiper Florida', descripcion = 'Departamento amplio, esta es una descripción de prueba',direccion = 'Calle Prueba #321',slug = 'hiper-florida',imagen_principal = None,valor_noche = '30000',abono_base = 0,id_ciu = '19111',id_est = '2824',id_pai = '44',capacidad = '4', id_tip = TIPOS_VIVIENDAS[0], internet = '1', luz = '1' , gas = '1', agua = '1'),
]

DETALLES_PROYECTOS : list[DetProyecto] = [
    DetProyecto(id_viv = VIVIENDAS[0], id_emp = EMPLEADOS[5]),
    DetProyecto(id_viv = VIVIENDAS[1], id_emp = EMPLEADOS[6]),
]

# Diccionario con los modelos de la base de datos
ENTITY = {
    'GRUPO' : GRUPOS,
    'GENERO' : GENEROS,
    'MODELO' : MODELOS,
    'CARGOS' : CARGOS,
    'COLOR' : COLORES,
    'MARCA' : MARCAS,
    'ROL_USUARIO' : ROLES,
    'CATEGORIA' : CATEGORIAS,
    'TIPO_VIVIENDA' : TIPOS_VIVIENDAS,
    'TIPO_SERVICIO' : TIPOS_SERVICIOS,
    'TIPO_DOCUMENTO' : TIPOS_DOCUMENTOS,
    'ESTADO_CIVIL' : ESTADO_CIVILES,
    'SALA' : SALAS,
    'DISPONIBILIDAD' : DISPONIBILIDADES,
    'ESTADO_PRODUCTO' : ESTADOS_PRODUCTOS,
    'DOCUMENTO_IDENTIDAD' : DOCUMENTOS_IDENTIDAD,
    'PRODUCTO' : PRODUCTOS,
    'PERSONA' : PERSONAS,
    'EMPLEADO' : EMPLEADOS,
    'VEHICULO' : VEHICULOS,
    'CONDUCTOR' : CONDUCTORES,
    'USUARIO' : USUARIOS,
    'VIVIENDA' : VIVIENDAS,
    'TIPO_UBICACION' : TIPOS_UBICACIONES,
    'UBICACION_TRANSPORTE' : UBICACIONES_TRANSPORTES,
    'DETALLE_PROYECTO' : DETALLES_PROYECTOS,
    'CLIENTE' : CLIENTES,
}

def save_entity(model_name : str):
    for generic in ENTITY[model_name]:
        generic.save()

def delete_objects(table_name):
    with connections['turismo_real'].cursor() as cursor:
            cursor.callproc("PKG_UTILS.SP_TRUNCATE_TABLE",[table_name])     

def run_seed():
    try:
        for key in reversed(ENTITY.keys()):
            delete_objects(ENTITY[key][0]._meta.db_table)

        for key in ENTITY.keys():
            print(key)
            save_entity(key)
        return True
    except:
        return False

## TODO: ELIMINAR CLIENTES DE PRUEBA, RESERVAS DE PRUEBA