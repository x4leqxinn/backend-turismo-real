from apps.base.models.db_models import *
from apps.users.models import User, UserRole

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
    Color(nombre = 'Azul')
]

MODELOS : list[Modelo] = [
    Modelo(nombre = 'ÑUÑUKI'),
    Modelo(nombre = 'AUDI')
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
    Persona(run = '20281676',dv = '2', nombre = 'Jorge' , snombre = 'Alejandro' ,
    ap_paterno = 'Quintui', ap_materno = 'Vergara', fecha_nacimiento = '2000-10-02',
    telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal',
    id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0],
    id_ciu = '1', id_est = '1', id_pai = '1')
]

EMPLEADOS : list[Empleado] = [
    Empleado(id = PERSONAS[0], sueldo = 99999, fecha_contrato = '2022-08-01', id_car = CARGOS[1]),
]


def get_user(email : str, role : UserRole, person : Persona, password : str) -> User:
    user = User(email = email, role = role, person = person, is_staff = True, is_superuser = True)
    user.set_password(password)
    return user

USUARIOS : list[User] = [
    get_user('jorgealequinn@gmail.com',ROLES[0],PERSONAS[0],'Admin123!'),
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

# Vivienda

VIVIENDAS : list[Vivienda] = [
    Vivienda(latitud = '-33.5342',longitud = '-70.59299',m2 = '53.45',estrellas = None,id_dis = DISPONIBILIDADES[0], nombre = 'Gran Avenida', descripcion = 'Departamento amplio, esta es una descripción de prueba',direccion = 'Calle Prueba #123',slug = 'gran-avenida',imagen_principal = None,valor_noche = '50000',abono_base = 0,id_ciu = '19111', id_est = '2824',id_pai = '44',capacidad = '3', id_tip = TIPOS_VIVIENDAS[0], internet = '1', luz = '1' , gas = '1', agua = '1'),
    Vivienda(latitud = '-33.5342',longitud = '-70.59299',m2 = '23.45',estrellas = None,id_dis = DISPONIBILIDADES[0], nombre = 'Hiper Florida', descripcion = 'Departamento amplio, esta es una descripción de prueba',direccion = 'Calle Prueba #321',slug = 'hiper-florida',imagen_principal = None,valor_noche = '30000',abono_base = 0,id_ciu = '19111',id_est = '2824',id_pai = '44',capacidad = '4', id_tip = TIPOS_VIVIENDAS[0], internet = '1', luz = '1' , gas = '1', agua = '1'),
]

# Diccionario con los modelos de la base de datos
ENTITY = {
    'GENERO' : GENEROS,
    'MODELO' : MODELOS,
    'CARGOS' : CARGOS,
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
    'USUARIO' : USUARIOS,
    'VIVIENDA' : VIVIENDAS
}

def save_entity(model_name : str):
    for generic in ENTITY[model_name]:
        generic.save()

def run_seed():
    for key in ENTITY.keys():
        print(key)
        save_entity(key)
    

