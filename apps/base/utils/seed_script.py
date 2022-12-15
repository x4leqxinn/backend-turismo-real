from apps.base.models.db_models import *
from apps.users.models import User, UserRole
from django.contrib.auth.models import Group
from django.db import connections
#from administration interface


TRAMO_MULTAS : list[TramoMulta] = [
    TramoMulta(estado_prod = 1, porcentaje = 0),
    TramoMulta(estado_prod = 2, porcentaje = 20),
    TramoMulta(estado_prod = 3, porcentaje = 40),
    TramoMulta(estado_prod = 4, porcentaje = 60),
    TramoMulta(estado_prod = 5, porcentaje = 80),
    TramoMulta(estado_prod = 6, porcentaje = 100),
]

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
    Disponibilidad(descripcion = 'EN MANTENCION'),
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
    Persona(run = '19294703',dv = '1', nombre = 'Matías' , snombre = 'a' , ap_paterno = 'Menares', ap_materno = 'ijd', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    Persona(run = '19083874',dv = '6', nombre = 'Alfonso' , snombre = 'a' , ap_paterno = 'Pacheco', ap_materno = 'ijd', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    Persona(run = '20262947',dv = '3', nombre = 'Tomás' , snombre = 'a' , ap_paterno = 'Campos', ap_materno = 'fjklsdj', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    Persona(run = '19047843',dv = '5', nombre = 'Francisco' , snombre = 'a' , ap_paterno = 'Pizarro', ap_materno = 'fjklsdj', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    Persona(run = '17948473',dv = '4', nombre = 'Paula' , snombre = 'a' , ap_paterno = 'Bonnet', ap_materno = 'fjklsdj', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    Persona(run = '18847834',dv = '2', nombre = 'Franco' , snombre = 'a' , ap_paterno = 'Villanueva', ap_materno = 'fjklsdj', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),

    ## RECEPCIONISTAS
    Persona(run = '19849395',dv = 'k', nombre = 'Carolina' , snombre = 'Uno' , ap_paterno = 'Díaz', ap_materno = 'Prueba', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    Persona(run = '19377494',dv = '1', nombre = 'Catalina' , snombre = 'Dos' , ap_paterno = 'Flores', ap_materno = 'Prueba', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    Persona(run = '19848433',dv = '5', nombre = 'Daniel' , snombre = 'Tres' , ap_paterno = 'Castillo', ap_materno = 'Prueba', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    Persona(run = '19474374',dv = '3', nombre = 'Macarena' , snombre = 'Cuatro' , ap_paterno = 'Bravo', ap_materno = 'Prueba', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    Persona(run = '19849023',dv = '8', nombre = 'Alondra' , snombre = 'Cinco' , ap_paterno = 'Rivas', ap_materno = 'Prueba', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    Persona(run = '19376473',dv = '3', nombre = 'Rodrigo' , snombre = 'Seis' , ap_paterno = 'Alvarez', ap_materno = 'Prueba', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),

    ## CLIENTES PARA TEST
    Persona(run = '18683444',dv = '7', nombre = 'Cliente' , snombre = 'Prueba' , ap_paterno = 'Prueba', ap_materno = 'Prueba', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '19081', id_est = '2824', id_pai = '44'),
    Persona(run = '18844764',dv = '9', nombre = 'Cliente' , snombre = 'Prueba' , ap_paterno = 'Prueba', ap_materno = 'Prueba', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '18955', id_est = '2830', id_pai = '44'),
    Persona(run = '19940043',dv = '0', nombre = 'Cliente' , snombre = 'Prueba' , ap_paterno = 'Prueba', ap_materno = 'Prueba', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '18952', id_est = '2832', id_pai = '44'),
    Persona(run = '19843989',dv = '2', nombre = 'Cliente' , snombre = 'Prueba' , ap_paterno = 'Prueba', ap_materno = 'Prueba', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '19022', id_est = '2834', id_pai = '44'),
    Persona(run = '19873730',dv = '3', nombre = 'Cliente' , snombre = 'Prueba' , ap_paterno = 'Prueba', ap_materno = 'Prueba', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '80923', id_est = '3681', id_pai = '173'),
    Persona(run = '19373749',dv = '6', nombre = 'Cliente' , snombre = 'Prueba' , ap_paterno = 'Prueba', ap_materno = 'Prueba', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '63983', id_est = '823', id_pai = '109'),
    Persona(run = '19089384',dv = '7', nombre = 'Cliente' , snombre = 'Prueba' , ap_paterno = 'Prueba', ap_materno = 'Prueba', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '14013', id_est = '1997', id_pai = '31'),
]

EMPLEADOS : list[Empleado] = [
    Empleado(id = PERSONAS[0], sueldo = 2000000, fecha_contrato = '2022-08-01', id_car = CARGOS[1]),
    Empleado(id = PERSONAS[1], sueldo = 2000000, fecha_contrato = '2022-08-01', id_car = CARGOS[1]),
    Empleado(id = PERSONAS[2], sueldo = 2000000, fecha_contrato = '2022-08-01', id_car = CARGOS[1]),
    Empleado(id = PERSONAS[3], sueldo = 2000000, fecha_contrato = '2022-08-01', id_car = CARGOS[1]),
    Empleado(id = PERSONAS[4], sueldo = 2000000, fecha_contrato = '2022-08-01', id_car = CARGOS[1]),
    ## Conductores
    Empleado(id = PERSONAS[5], sueldo = 700000, fecha_contrato = '2022-08-01', id_car = CARGOS[3]),
    Empleado(id = PERSONAS[6], sueldo = 700000, fecha_contrato = '2022-08-01', id_car = CARGOS[3]),
    Empleado(id = PERSONAS[7], sueldo = 650000, fecha_contrato = '2022-08-01', id_car = CARGOS[3]),
    Empleado(id = PERSONAS[8], sueldo = 650000, fecha_contrato = '2022-08-01', id_car = CARGOS[3]),
    Empleado(id = PERSONAS[9], sueldo = 600000, fecha_contrato = '2022-08-01', id_car = CARGOS[3]),
    Empleado(id = PERSONAS[10], sueldo = 600000, fecha_contrato = '2022-08-01', id_car = CARGOS[3]),

    ## Recepcionistas
    Empleado(id = PERSONAS[11], sueldo = 650000, fecha_contrato = '2022-08-01', id_car = CARGOS[2]),
    Empleado(id = PERSONAS[12], sueldo = 600000, fecha_contrato = '2022-08-01', id_car = CARGOS[2]),
    Empleado(id = PERSONAS[13], sueldo = 600000, fecha_contrato = '2022-08-01', id_car = CARGOS[2]),
    Empleado(id = PERSONAS[14], sueldo = 650000, fecha_contrato = '2022-08-01', id_car = CARGOS[2]),
    Empleado(id = PERSONAS[15], sueldo = 600000, fecha_contrato = '2022-08-01', id_car = CARGOS[2]),
    Empleado(id = PERSONAS[16], sueldo = 600000, fecha_contrato = '2022-08-01', id_car = CARGOS[2]),
]

RECEPCIONISTAS : list[Recepcionista] = [
    Recepcionista(id = EMPLEADOS[11]),
    Recepcionista(id = EMPLEADOS[12]),
    Recepcionista(id = EMPLEADOS[13]),
    Recepcionista(id = EMPLEADOS[14]),
    Recepcionista(id = EMPLEADOS[15]),
    Recepcionista(id = EMPLEADOS[16]),
]

VEHICULOS : list[Vehiculo] = [
    Vehiculo(patente = 'AO32FNV', id_mod = MODELOS[0], id_mar = MARCAS[0], id_col = COLORES[0], capacidad = 5, imagen = None),
    Vehiculo(patente = 'XDJN72', id_mod = MODELOS[1], id_mar = MARCAS[1], id_col = COLORES[1], capacidad = 5, imagen = None),
    Vehiculo(patente = 'AIN54NL', id_mod = MODELOS[1], id_mar = MARCAS[1], id_col = COLORES[1], capacidad = 5, imagen = None),
    Vehiculo(patente = 'AHNH456', id_mod = MODELOS[1], id_mar = MARCAS[1], id_col = COLORES[1], capacidad = 5, imagen = None),
    Vehiculo(patente = 'SHNR732', id_mod = MODELOS[1], id_mar = MARCAS[1], id_col = COLORES[1], capacidad = 5, imagen = None),
    Vehiculo(patente = 'AOS2383', id_mod = MODELOS[1], id_mar = MARCAS[1], id_col = COLORES[1], capacidad = 5, imagen = None),
]

CONDUCTORES : list[Conductor] = [
    Conductor(id = EMPLEADOS[5], id_veh = VEHICULOS[0]),
    Conductor(id = EMPLEADOS[6], id_veh = VEHICULOS[1]),
    Conductor(id = EMPLEADOS[7], id_veh = VEHICULOS[2]),
    Conductor(id = EMPLEADOS[8], id_veh = VEHICULOS[3]),
    Conductor(id = EMPLEADOS[9], id_veh = VEHICULOS[4]),
    Conductor(id = EMPLEADOS[10], id_veh = VEHICULOS[5]),
]

CLIENTES : list[Cliente] = [
    Cliente(id = PERSONAS[17]),
    Cliente(id = PERSONAS[18]),
    Cliente(id = PERSONAS[19]),
    Cliente(id = PERSONAS[20]),
    Cliente(id = PERSONAS[21]),
    Cliente(id = PERSONAS[22]),
    Cliente(id = PERSONAS[23]),
]

def get_user(email : str, role : UserRole, person : Persona, password : str) -> User:
    user = User(email = email, role = role, person = person, is_staff = False, is_superuser = False)
    user.set_password(password)
    return user

def get_admin_user(email : str, role : UserRole, person : Persona, password : str) -> User:
    user = User(email = email, role = role, person = person, is_staff = True, is_superuser = True)
    user.set_password(password)
    return user

USUARIOS : list[User] = [
    ## ADMINS
    get_admin_user('jorge@gmail.com',ROLES[0],PERSONAS[0],'Admin123!'),
    get_admin_user('lucasmenaresaguirre@gmail.com',ROLES[0],PERSONAS[1],'Admin123!'),
    get_admin_user('paulasotoretamal@gmail.com',ROLES[0],PERSONAS[2],'Admin123!'),
    get_admin_user('joaking.twitch001@gmail.com',ROLES[0],PERSONAS[3],'Admin123!'),
    get_admin_user('paulapinamarin@gmail.com',ROLES[0],PERSONAS[4],'Admin123!'),
    
    ## DRIVERS
    get_user('jorgealequinn@gmail.com',ROLES[1],PERSONAS[5],'Admin123!'),
    get_user('conductor2@gmail.com',ROLES[1],PERSONAS[6],'Admin123!'),
    get_user('conductor3@gmail.com',ROLES[1],PERSONAS[7],'Admin123!'),
    get_user('conductor4@gmail.com',ROLES[1],PERSONAS[8],'Admin123!'),
    get_user('conductor5@gmail.com',ROLES[1],PERSONAS[9],'Admin123!'),
    get_user('conductor6@gmail.com',ROLES[1],PERSONAS[10],'Admin123!'),
    
    ## RECEPTIONISTS
    get_user('jo.quintui@duocuc.cl',ROLES[1],PERSONAS[11],'Admin123!'),
    get_user('recepcionista2@gmail.com',ROLES[1],PERSONAS[12],'Admin123!'),
    get_user('recepcionista3@gmail.com',ROLES[1],PERSONAS[13],'Admin123!'),
    get_user('recepcionista4@gmail.com',ROLES[1],PERSONAS[14],'Admin123!'),
    get_user('recepcionista5@gmail.com',ROLES[1],PERSONAS[15],'Admin123!'),
    get_user('recepcionista6@gmail.com',ROLES[1],PERSONAS[16],'Admin123!'),

    ## CLIENTS
    get_user('cliente1@gmail.com',ROLES[2],PERSONAS[17],'Admin123!'),
    get_user('cliente2@gmail.com',ROLES[2],PERSONAS[18],'Admin123!'),
    get_user('cliente3@gmail.com',ROLES[2],PERSONAS[19],'Admin123!'),
    get_user('cliente4@gmail.com',ROLES[2],PERSONAS[20],'Admin123!'),
    get_user('cliente5@gmail.com',ROLES[2],PERSONAS[21],'Admin123!'),
    get_user('cliente6@gmail.com',ROLES[2],PERSONAS[22],'Admin123!'),
    get_user('cliente7@gmail.com',ROLES[2],PERSONAS[23],'Admin123!'),
]

PRODUCTOS : list[Producto] = [
    Producto(id_cat = CATEGORIAS[1],descripcion ='Televisor', precio = 200000),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Cocina',precio = 150000),
    Producto(id_cat = CATEGORIAS[1],descripcion = 'Refrigerador',precio = 200000),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Ducha',precio = 50000),
    Producto(id_cat = CATEGORIAS[1],descripcion = 'Microondas',precio = 20000),
    Producto(id_cat = CATEGORIAS[1],descripcion = 'Aspiradora',precio = 10000),
    Producto(id_cat = CATEGORIAS[1],descripcion = 'Juguera',precio = 10000),
    Producto(id_cat = CATEGORIAS[1],descripcion = 'Tostador',precio = 10000),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Velador',precio = 35000),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Cómoda',precio = 40000),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Clóset',precio = 40000),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Escritorio',precio = 70000),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Armario',precio = 70000),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Estante',precio = 80000),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Sofá',precio = 100000),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Cama 2 plazas',precio = 200000),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Cama individual',precio = 100000),
    Producto(id_cat = CATEGORIAS[0],descripcion = 'Mesa ',precio = 130000),
    Producto(id_cat = CATEGORIAS[2],descripcion = 'Secador ',precio = 10000),
    Producto(id_cat = CATEGORIAS[2],descripcion = 'Depilador',precio = 10000),
    Producto(id_cat = CATEGORIAS[2],descripcion = 'Plancha alisadora',precio = 15000),
    Producto(id_cat = CATEGORIAS[2],descripcion = 'Afeitadora',precio = 30000),
    Producto(id_cat = CATEGORIAS[1],descripcion = 'Lavadora',precio = 200000)
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
    TipoUbicacion(descripcion = 'Recorrido'),
]

UBICACIONES_TRANSPORTES : list[UbicacionTrans] = [
    UbicacionTrans(categoria = 'TRANSPORTE', nombre = 'Aeropuerto Arturo Merino Benitez', precio = 20000, latitud = '72387', longitud = '423423', id_tip = TIPOS_UBICACIONES[0], id_ciu = 19111),
    UbicacionTrans(categoria = 'TRANSPORTE', nombre = 'Terminal de buses Centro', precio = 20000, latitud = '72387', longitud = '423423', id_tip = TIPOS_UBICACIONES[0], id_ciu = 19111),
    UbicacionTrans(categoria = 'TRANSPORTE', nombre = 'Terminal de buses Viña Centro', precio = 10000, latitud = '72387', longitud = '423423', id_tip = TIPOS_UBICACIONES[0], id_ciu = 19130),
    UbicacionTrans(categoria = 'TRANSPORTE', nombre = 'Terminal de buses Viña Norte ', precio = 20000, latitud = '72387', longitud = '423423', id_tip = TIPOS_UBICACIONES[1], id_ciu = 19130),
    UbicacionTrans(categoria = 'TOUR', nombre = 'Tour Viña ', precio = 20000, latitud = '72387', longitud = '423423', id_tip = TIPOS_UBICACIONES[2], id_ciu = 19130),
    UbicacionTrans(categoria = 'TOUR', nombre = 'Tour Valparaíso ', precio = 30000, latitud = '72387', longitud = '423423', id_tip = TIPOS_UBICACIONES[2], id_ciu = 19130),
    UbicacionTrans(categoria = 'TRANSPORTE', nombre = 'Terminal de buses Pucón Sur', precio = 10000, latitud = '72387', longitud = '423423', id_tip = TIPOS_UBICACIONES[0], id_ciu = 19080),
    UbicacionTrans(categoria = 'TRANSPORTE', nombre = 'Terminal de buses Serena', precio = 10000, latitud = '72387', longitud = '423423', id_tip = TIPOS_UBICACIONES[0], id_ciu = 18994),
    UbicacionTrans(categoria = 'TRANSPORTE', nombre = 'Aeropuerto La Serena', precio = 20000, latitud = '72387', longitud = '423423', id_tip = TIPOS_UBICACIONES[1], id_ciu = 18994),
    UbicacionTrans(categoria = 'TRANSPORTE', nombre = 'Terminal de buses Varas Centro', precio = 10000, latitud = '72387', longitud = '423423', id_tip = TIPOS_UBICACIONES[0], id_ciu = 19087),
    UbicacionTrans(categoria = 'TRANSPORTE', nombre = 'Aeropuerto Puerto Varas', precio = 20000, latitud = '72387', longitud = '423423', id_tip = TIPOS_UBICACIONES[1], id_ciu = 19087),
    UbicacionTrans(categoria = 'TOUR', nombre = 'Tour de prueba', precio = 20000, latitud = '72387', longitud = '423423', id_tip = TIPOS_UBICACIONES[2], id_ciu = 19087),
]

VIVIENDAS : list[Vivienda] = [
    Vivienda(latitud = '-33.01908',longitud = '-71.55206',m2 = '53.45',estrellas = 5,id_dis = DISPONIBILIDADES[0], nombre = 'Gran Avenida', descripcion = 'Departamento amplio, esta es una descripción de prueba',direccion = 'Barrio Prueba #123',slug = 'gran-avenida',imagen_principal = "viviendas/gran-avenida.jpg",valor_noche = '50000',abono_base = 0,id_ciu = '19130', id_est = '2824',id_pai = '44',capacidad = '3', id_tip = TIPOS_VIVIENDAS[0], internet = '1', luz = '1' , gas = '1', agua = '1'),
    Vivienda(latitud = '-39.27761',longitud = '-71.97157',m2 = '52.15',estrellas = 5,id_dis = DISPONIBILIDADES[0], nombre = 'Oye Pucón', descripcion = 'Departamento amplio, esta es una descripción de prueba',direccion = 'Barrio Prueba #531',slug = 'oye-pucon',imagen_principal = "viviendas/oye-pucon.jpg",valor_noche = '55000',abono_base = 0,id_ciu = '19080',id_est = '2824',id_pai = '44',capacidad = '3', id_tip = TIPOS_VIVIENDAS[0], internet = '1', luz = '1' , gas = '1', agua = '1'),
    Vivienda(latitud = '-33.01015',longitud = '-71.55120',m2 = '43.45',estrellas = 4,id_dis = DISPONIBILIDADES[0], nombre = 'Hiper Playa', descripcion = 'Departamento amplio, esta es una descripción de prueba',direccion = 'Barrio Prueba #321',slug = 'hiper-playa',imagen_principal = "viviendas/hiper-playa.jpg",valor_noche = '30000',abono_base = 0,id_ciu = '19130',id_est = '2824',id_pai = '44',capacidad = '4', id_tip = TIPOS_VIVIENDAS[0], internet = '1', luz = '1' , gas = '1', agua = '1'),
    Vivienda(latitud = '-29.93463',longitud = '-71.26074',m2 = '55.45',estrellas = 4,id_dis = DISPONIBILIDADES[0], nombre = 'Serena Grande', descripcion = 'Departamento amplio, esta es una descripción de prueba',direccion = 'Barrio Prueba #563',slug = 'serena-grande',imagen_principal = "viviendas/serena-grande.jpg",valor_noche = '20000',abono_base = 0,id_ciu = '18994',id_est = '2824',id_pai = '44',capacidad = '2', id_tip = TIPOS_VIVIENDAS[0], internet = '1', luz = '1' , gas = '1', agua = '1'),
    Vivienda(latitud = '-41.32745',longitud = '-72.97340',m2 = '59.15',estrellas = 5,id_dis = DISPONIBILIDADES[0], nombre = 'Puerto Lindo', descripcion = 'Departamento amplio, esta es una descripción de prueba',direccion = 'Barrio Prueba #421',slug = 'puerto-lindo',imagen_principal = "viviendas/puerto-lindo.jpg",valor_noche = '30000',abono_base = 0,id_ciu = '19087',id_est = '2824',id_pai = '44',capacidad = '3', id_tip = TIPOS_VIVIENDAS[0], internet = '1', luz = '1' , gas = '1', agua = '1'),
    Vivienda(latitud = '-33.42929',longitud = '-70.59055',m2 = '69.15',estrellas = 4,id_dis = DISPONIBILIDADES[0], nombre = 'Provi Grande', descripcion = 'Departamento amplio, esta es una descripción de prueba',direccion = 'Barrio Prueba #444',slug = 'provi-grande',imagen_principal = "viviendas/provi-grande.jpg",valor_noche = '70000',abono_base = 0,id_ciu = '19111',id_est = '2824',id_pai = '44',capacidad = '3', id_tip = TIPOS_VIVIENDAS[0], internet = '1', luz = '1' , gas = '1', agua = '1'),
]

DETALLES_PROYECTOS : list[DetProyecto] = [
    ## GRAN AVENIDA
    ## DRIVERS 
    DetProyecto(id_viv = VIVIENDAS[0], id_emp = EMPLEADOS[5]),
    ## RECEPTIONISTS
    DetProyecto(id_viv = VIVIENDAS[0], id_emp = EMPLEADOS[11]),

    ## Oe pucon
    ## DRIVERS 
    DetProyecto(id_viv = VIVIENDAS[1], id_emp = EMPLEADOS[6]),
    ## RECEPTIONISTS
    DetProyecto(id_viv = VIVIENDAS[1], id_emp = EMPLEADOS[12]),

    # Hiperplaya
    ## DRIVERS 
    DetProyecto(id_viv = VIVIENDAS[2], id_emp = EMPLEADOS[7]),
    ## RECEPTIONISTS
    DetProyecto(id_viv = VIVIENDAS[2], id_emp = EMPLEADOS[13]),

    ## Serena grande
    ## DRIVERS 
    DetProyecto(id_viv = VIVIENDAS[3], id_emp = EMPLEADOS[8]),
    ## RECEPTIONISTS
    DetProyecto(id_viv = VIVIENDAS[3], id_emp = EMPLEADOS[14]),

    ## Puerto lindo
    ## DRIVERS 
    DetProyecto(id_viv = VIVIENDAS[4], id_emp = EMPLEADOS[9]),
    ## RECEPTIONISTS
    DetProyecto(id_viv = VIVIENDAS[4], id_emp = EMPLEADOS[15]),

    ## Provi grande
    ## DRIVERS 
    DetProyecto(id_viv = VIVIENDAS[5], id_emp = EMPLEADOS[10]),
    ## RECEPTIONISTS
    DetProyecto(id_viv = VIVIENDAS[5], id_emp = EMPLEADOS[16]),
]

GALERIAS_EXTERIORES : list[GaleriaExterior] = [
    GaleriaExterior(id_viv = VIVIENDAS[0], imagen = 'exterior_gallery/gran-avenida.jpg'),
    GaleriaExterior(id_viv = VIVIENDAS[1], imagen = 'exterior_gallery/oye-pucon.jpg'),
    GaleriaExterior(id_viv = VIVIENDAS[2], imagen = 'exterior_gallery/hiper-playa.jpg'),
    GaleriaExterior(id_viv = VIVIENDAS[3], imagen = 'exterior_gallery/serena-grande.jpg'),
    GaleriaExterior(id_viv = VIVIENDAS[4], imagen = 'exterior_gallery/puerto-lindo.jpg'),
    GaleriaExterior(id_viv = VIVIENDAS[5], imagen = 'exterior_gallery/provi-grande.jpg'),
]

GALERIAS_INTERIORES : list[GaleriaInterior] = [
    ## Gran Avenida
    GaleriaInterior(id_viv = VIVIENDAS[0], imagen = 'interior_gallery/gran-avenida-1.jpg'),
    GaleriaInterior(id_viv = VIVIENDAS[0], imagen = 'interior_gallery/gran-avenida-2.jpg'),
    ## Oye Pucon
    GaleriaInterior(id_viv = VIVIENDAS[1], imagen = 'interior_gallery/oye-pucon-1.jpg'),
    GaleriaInterior(id_viv = VIVIENDAS[1], imagen = 'interior_gallery/oye-pucon-2.jpg'),
    ## Hiper Playa
    GaleriaInterior(id_viv = VIVIENDAS[2], imagen = 'interior_gallery/hiper-playa-1.jpeg'),
    ## Serena Grande
    GaleriaInterior(id_viv = VIVIENDAS[3], imagen = 'interior_gallery/serena-grande-1.jpeg'),
    ## Puerto Lindo
    GaleriaInterior(id_viv = VIVIENDAS[4], imagen = 'interior_gallery/puerto-lindo-1.jpeg'),
    ## Provi Grande
    GaleriaInterior(id_viv = VIVIENDAS[5], imagen = 'interior_gallery/provi-grande-1.jpeg'),
]

INVENTARIOS : list[Inventario] = [
    ## Gran Avenida
    Inventario(id_viv = VIVIENDAS[0]),
    ## Oye Pucon
    Inventario(id_viv = VIVIENDAS[1]),
    ## Hiper Playa
    Inventario(id_viv = VIVIENDAS[2]),
    ## Serena Grande
    Inventario(id_viv = VIVIENDAS[3]),
    ## Puerto Lindo
    Inventario(id_viv = VIVIENDAS[4]),
    ## Provi Grande
    Inventario(id_viv = VIVIENDAS[5]),
]

DETALLES_SALAS : list[DetalleSala] = [
    ## Gran Avenida
    DetalleSala(id_inv = INVENTARIOS[0], id_sal = SALAS[0], imagen_sala = 'interior_gallery/gran-avenida-1.jpg'),
    DetalleSala(id_inv = INVENTARIOS[0], id_sal = SALAS[5], imagen_sala = 'rooms/gran-avenida-dorm-1.jpg'),
    DetalleSala(id_inv = INVENTARIOS[0], id_sal = SALAS[5], imagen_sala = 'rooms/gran-avenida-dorm-2.jpg'),
    ## Oye Pucon
    DetalleSala(id_inv = INVENTARIOS[1], id_sal = SALAS[0], imagen_sala = 'interior_gallery/oye-pucon-1.jpg'),
    DetalleSala(id_inv = INVENTARIOS[1], id_sal = SALAS[5], imagen_sala = 'rooms/oye-pucon-dorm-1.jpeg'),
    DetalleSala(id_inv = INVENTARIOS[1], id_sal = SALAS[5], imagen_sala = 'rooms/oye-pucon-dorm-2.jpeg'),
    DetalleSala(id_inv = INVENTARIOS[1], id_sal = SALAS[1], imagen_sala = 'rooms/oye-pucon-cocina-1.jpeg'),
    ## Hiper Playa
    DetalleSala(id_inv = INVENTARIOS[2], id_sal = SALAS[0], imagen_sala = 'interior_gallery/hiper-playa-1.jpeg'),
    DetalleSala(id_inv = INVENTARIOS[2], id_sal = SALAS[5], imagen_sala = 'rooms/hiper-playa-dorm-1.jpeg'),
    DetalleSala(id_inv = INVENTARIOS[2], id_sal = SALAS[4], imagen_sala = 'rooms/hiper-playa-balcon-1.jpeg'),
    ## Serena Grande
    DetalleSala(id_inv = INVENTARIOS[3], id_sal = SALAS[0], imagen_sala = 'interior_gallery/serena-grande-1.jpeg'),
    DetalleSala(id_inv = INVENTARIOS[3], id_sal = SALAS[5], imagen_sala = 'rooms/gran-avenida-dorm-1.jpg'),
    DetalleSala(id_inv = INVENTARIOS[3], id_sal = SALAS[5], imagen_sala = 'rooms/gran-avenida-dorm-2.jpg'),
    ## Puerto Lindo
    DetalleSala(id_inv = INVENTARIOS[4], id_sal = SALAS[0], imagen_sala = 'interior_gallery/puerto-lindo-1.jpeg'),
    DetalleSala(id_inv = INVENTARIOS[4], id_sal = SALAS[5], imagen_sala = 'rooms/puerto-lindo-dorm-1.jpeg'),
    ## Provi Grande
    DetalleSala(id_inv = INVENTARIOS[5], id_sal = SALAS[0], imagen_sala = 'interior_gallery/provi-grande-1.jpeg'),
    DetalleSala(id_inv = INVENTARIOS[5], id_sal = SALAS[5], imagen_sala = 'rooms/oye-pucon-dorm-1.jpeg'),
    DetalleSala(id_inv = INVENTARIOS[5], id_sal = SALAS[5], imagen_sala = 'rooms/oye-pucon-dorm-2.jpeg'),
    DetalleSala(id_inv = INVENTARIOS[5], id_sal = SALAS[1], imagen_sala = 'rooms/oye-pucon-cocina-1.jpeg'),
]

DETALLE_PRODUCTOS : list[DetalleProducto] = [
    ## Gran Avenida
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[0], id_pro = PRODUCTOS[0]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[0], id_pro = PRODUCTOS[6]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[0], id_pro = PRODUCTOS[15]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[1], id_pro = PRODUCTOS[0]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[1], id_pro = PRODUCTOS[16]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[1], id_pro = PRODUCTOS[11]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[2], id_pro = PRODUCTOS[0]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[2], id_pro = PRODUCTOS[17]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[2], id_pro = PRODUCTOS[11]),
    ## Oye Pucon
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[3], id_pro = PRODUCTOS[0]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[3], id_pro = PRODUCTOS[6]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[3], id_pro = PRODUCTOS[15]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[4], id_pro = PRODUCTOS[0]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[4], id_pro = PRODUCTOS[16]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[4], id_pro = PRODUCTOS[11]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[5], id_pro = PRODUCTOS[0]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[5], id_pro = PRODUCTOS[17]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[5], id_pro = PRODUCTOS[11]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[6], id_pro = PRODUCTOS[1]),
    ## Hiper Playa
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[7], id_pro = PRODUCTOS[0]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[7], id_pro = PRODUCTOS[6]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[7], id_pro = PRODUCTOS[15]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[8], id_pro = PRODUCTOS[0]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[8], id_pro = PRODUCTOS[16]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[8], id_pro = PRODUCTOS[11]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[9], id_pro = PRODUCTOS[14]),
    ## Serena Grande
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[10], id_pro = PRODUCTOS[0]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[10], id_pro = PRODUCTOS[6]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[10], id_pro = PRODUCTOS[15]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[11], id_pro = PRODUCTOS[0]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[11], id_pro = PRODUCTOS[16]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[11], id_pro = PRODUCTOS[11]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[12], id_pro = PRODUCTOS[0]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[12], id_pro = PRODUCTOS[17]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[12], id_pro = PRODUCTOS[11]),
    ## Puerto Lindo
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[13], id_pro = PRODUCTOS[0]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[13], id_pro = PRODUCTOS[6]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[13], id_pro = PRODUCTOS[15]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[14], id_pro = PRODUCTOS[0]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[14], id_pro = PRODUCTOS[16]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[14], id_pro = PRODUCTOS[11]),
    ## Provi Grande
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[15], id_pro = PRODUCTOS[0]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[15], id_pro = PRODUCTOS[15]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[16], id_pro = PRODUCTOS[0]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[16], id_pro = PRODUCTOS[16]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[17], id_pro = PRODUCTOS[0]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[17], id_pro = PRODUCTOS[11]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[18], id_pro = PRODUCTOS[1]),    
]

# Diccionario con los modelos de la base de datos
ENTITY = {
    'TRAMO_MULTA' : TRAMO_MULTAS,
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
    'RECEPCIONISTAS' : RECEPCIONISTAS,
    'VEHICULO' : VEHICULOS,
    'CONDUCTOR' : CONDUCTORES,
    'USUARIO' : USUARIOS,
    'VIVIENDA' : VIVIENDAS,
    'TIPO_UBICACION' : TIPOS_UBICACIONES,
    'UBICACION_TRANSPORTE' : UBICACIONES_TRANSPORTES,
    'DETALLE_PROYECTO' : DETALLES_PROYECTOS,
    'CLIENTE' : CLIENTES,
    'GALERIA_EXTERIOR' : GALERIAS_EXTERIORES,
    'GALERIA_INTERIOR' : GALERIAS_INTERIORES,
    'INVENTARIOS' : INVENTARIOS,
    'DETALLE_SALAS' : DETALLES_SALAS,
    'DETALLE_PRODUCTOS' : DETALLE_PRODUCTOS,
}

def save_entity(model_name : str):
    for generic in ENTITY[model_name]:
        generic.save()

def delete_objects(table_name):
    with connections['turismo_real'].cursor() as cursor:
        cursor.callproc("PKG_UTILS.SP_TRUNCATE_TABLE",[table_name])    

def run_dataframe():
    with connections['turismo_real'].cursor() as cursor:
        cursor.callproc("dbms_scheduler.run_job",['JOB_MACHINE_LEARNING']) 

def run_seed():
    try:
        for key in reversed(ENTITY.keys()):
            delete_objects(ENTITY[key][0]._meta.db_table)

        for key in ENTITY.keys():
            print(key)
            save_entity(key)
        
        run_dataframe()

        return True
    except Exception as e:
        print(e)
        return False

