from apps.base.models.db_models import *
from apps.users.models import User, UserRole
from django.contrib.auth.models import Group
from django.db import connections
#from administration interface

## DJANGO ADMIN
#TEMAS : list[The]


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
    Persona(run = '11111111',dv = '1', nombre = 'Matias' , snombre = 'a' , ap_paterno = 'Menares', ap_materno = 'ijd', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    Persona(run = '22222222',dv = '1', nombre = 'Alfonso' , snombre = 'a' , ap_paterno = 'Pacheco', ap_materno = 'fjklsdj', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),

    ## RECEPCIONISTAS
    Persona(run = '33333333',dv = '1', nombre = 'Recepcionista' , snombre = 'Uno' , ap_paterno = 'Prueba', ap_materno = 'Prueba', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    Persona(run = '44444444',dv = '1', nombre = 'Recepcionista' , snombre = 'Dos' , ap_paterno = 'Prueba', ap_materno = 'Prueba', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    #Persona(run = '22222222',dv = '1', nombre = 'Alfonso' , snombre = 'a' , ap_paterno = 'Pacheco', ap_materno = 'Marin', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    #Persona(run = '22222222',dv = '1', nombre = 'Alfonso' , snombre = 'a' , ap_paterno = 'Pacheco', ap_materno = 'Marin', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
    
    ## CLIENTES PARA TEST
    Persona(run = '55555555',dv = '1', nombre = 'Cliente' , snombre = 'Prueba' , ap_paterno = 'Prueba', ap_materno = 'Prueba', fecha_nacimiento = '2000-10-02', telefono = '965928439', num_calle = '1705', calle = 'Cerro Paranal', id_gen = GENEROS[0], id_doc = DOCUMENTOS_IDENTIDAD[0], id_est1 = ESTADO_CIVILES[0], id_ciu = '1', id_est = '1', id_pai = '1'),
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
    ## Recepcionistas
    Empleado(id = PERSONAS[7], sueldo = 99999, fecha_contrato = '2022-08-01', id_car = CARGOS[2]),
    Empleado(id = PERSONAS[8], sueldo = 99999, fecha_contrato = '2022-08-01', id_car = CARGOS[2]),
]

RECEPCIONISTAS : list[Recepcionista] = [
    Recepcionista(id = EMPLEADOS[7]),
    Recepcionista(id = EMPLEADOS[8]),
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
    get_user('recepcionista1@gmail.com',ROLES[1],PERSONAS[7],'Recepcionista123!'),
    get_user('recepcionista2@gmail.com',ROLES[1],PERSONAS[8],'Recepcionista123!'),
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
    UbicacionTrans(categoria = 'TRANSPORTE', nombre = 'Aeropuerto Viña del Mar ', precio = 20000, latitud = '72387', longitud = '423423', id_tip = TIPOS_UBICACIONES[1], id_ciu = 19130),
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
    DetProyecto(id_viv = VIVIENDAS[0], id_emp = EMPLEADOS[5]),
    DetProyecto(id_viv = VIVIENDAS[1], id_emp = EMPLEADOS[6]),
    DetProyecto(id_viv = VIVIENDAS[0], id_emp = EMPLEADOS[7]),
    DetProyecto(id_viv = VIVIENDAS[1], id_emp = EMPLEADOS[8]),
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
    GaleriaInterior(id_viv = VIVIENDAS[0], imagen = 'interior_gallery/gran-avenida-1.jpg'),
    GaleriaInterior(id_viv = VIVIENDAS[0], imagen = 'interior_gallery/gran-avenida-2.jpg'),
    GaleriaInterior(id_viv = VIVIENDAS[1], imagen = 'interior_gallery/oye-pucon-1.jpg'),
    GaleriaInterior(id_viv = VIVIENDAS[1], imagen = 'interior_gallery/oye-pucon-2.jpg'),
]

INVENTARIOS : list[Inventario] = [
    Inventario(id_viv = VIVIENDAS[0]),
    Inventario(id_viv = VIVIENDAS[1]),
]

DETALLES_SALAS : list[DetalleSala] = [
    DetalleSala(id_inv = INVENTARIOS[0], id_sal = SALAS[0], imagen_sala = 'interior_gallery/gran-avenida-1.jpg'),
    DetalleSala(id_inv = INVENTARIOS[0], id_sal = SALAS[5], imagen_sala = 'rooms/gran-avenida-dorm-1.jpg'),
    DetalleSala(id_inv = INVENTARIOS[0], id_sal = SALAS[5], imagen_sala = 'rooms/gran-avenida-dorm-2.jpg'),
]

DETALLE_PRODUCTOS : list[DetalleProducto] = [
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[0], id_pro = PRODUCTOS[0]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[0], id_pro = PRODUCTOS[6]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[0], id_pro = PRODUCTOS[15]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[1], id_pro = PRODUCTOS[0]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[1], id_pro = PRODUCTOS[16]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[1], id_pro = PRODUCTOS[11]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[2], id_pro = PRODUCTOS[0]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[2], id_pro = PRODUCTOS[17]),
    DetalleProducto(id_est = ESTADOS_PRODUCTOS[0], id_det = DETALLES_SALAS[2], id_pro = PRODUCTOS[11]),
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
    except:
        return False

