from apps.base.models.db_models import *

CARGOS : list[Cargo] = [
    Cargo(descripcion = 'Administrador web'),
    Cargo(descripcion = 'Administrador de base de datos'),
    Cargo(descripcion = 'Recepcionista'),
    Cargo(descripcion = 'Conductor')
]

CATEGORIA : list[Categoria] = [
    Categoria(descripcion = 'Mobiliario'),
    Categoria(descripcion = 'Electrodoméstico'),
    Categoria(descripcion = 'Belleza')
]

DISPONIBILIDAD : list[Disponibilidad] = [
    Disponibilidad(descripcion = 'DISPONIBLE'),
    Disponibilidad(descripcion = 'NO DISPONIBLE')
]

COLOR : list[Color] = [
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

ESTADO_CIVIL : list[EstadoCivil] = [
    EstadoCivil(descripcion = 'SOLTERO/A'),
    EstadoCivil(descripcion = 'CASADO/A'),
    EstadoCivil(descripcion = 'COMPLICADO/A')
]

ESTADO_PRODUCTO : list[EstadoProducto] = [
    EstadoProducto(descripcion = 'PERFECTO'),
    EstadoProducto(descripcion = 'BUEN ESTADO'),
    EstadoProducto(descripcion = 'PARCIALMENTE DAÑADO'),
    EstadoProducto(descripcion = 'DAÑADO'),
    EstadoProducto(descripcion = 'MUY DAÑADO'),
    EstadoProducto(descripcion = 'INUTILIZABLE')
]

SALA : list[Sala] = [
    Sala(descripcion = 'LIVING'),
    Sala(descripcion = 'COCINA'),
    Sala(descripcion = 'COMEDOR'),
    Sala(descripcion = 'BAÑO'),
    Sala(descripcion = 'BALCÓN'),
    Sala(descripcion = 'DORMITORIO'),
    Sala(descripcion = 'ESTACIONAMIENTO')
]

PERSONA : list[Persona] = [
    Persona()
]

PRODUCTO : list[Producto] = [
    Producto(id_cat = CATEGORIA[1],descripcion ='Televisor', precio = 999),
    '''
    Producto(id_cat = '2',nombre = 'Cocina',precio = 99999),
    Producto(id_cat = '2',nombre = 'Refrigerador',precio = 99999),
    Producto(id_cat = '1',nombre = 'Ducha',precio = 99999),
    Producto(id_cat = '2',nombre = 'Microondas',precio = 99999),
    Producto(id_cat = '2',nombre = 'Aspiradora',precio = 99999),
    Producto(id_cat = '2',nombre = 'Juguera',precio = 99999),
    Producto(id_cat = '2',nombre = 'Tostador',precio = 99999),
    Producto(id_cat = '1',nombre = 'Velador',precio = 99999),
    Producto(id_cat = '1',nombre = 'Cómoda',precio = 99999),
    Producto(id_cat = '1',nombre = 'Clóset',precio = 99999),
    Producto(id_cat = '1',nombre = 'Escritorio',precio = 99999),
    Producto(id_cat = '1',nombre = 'Armario',precio = 99999),
    Producto(id_cat = '1',nombre = 'Estante',precio = 99999),
    Producto(id_cat = '1',nombre = 'Sofá',precio = 99999),
    Producto(id_cat = '1',nombre = 'Cama 2 plazas',precio = 99999),
    Producto(id_cat = '1',nombre = 'Cama individual',precio = 99999),
    Producto(id_cat = '1',nombre = 'Mesa ',precio = 99999),
    Producto(id_cat = '3',nombre = 'Secador ',precio = 99999),
    Producto(id_cat = '3',nombre = 'Depilador',precio = 99999),
    Producto(id_cat = '3',nombre = 'Plancha alisadora',precio = 99999),
    Producto(id_cat = '3',nombre = 'Afeitadora',precio = 99999),
    Producto(id_cat = '2',nombre = 'Lavadora',precio = 99999)
    '''
]


TIPO_DOCUMENTO : list[TipoDocumento] = [
    TipoDocumento(descripcion = 'CHECK IN'),
    TipoDocumento(descripcion = 'CHECK OUT'),
    TipoDocumento(descripcion = 'CHECK COORDINACION')
]

TIPO_VIVIENDA : list[TipoVivienda] = [
    TipoVivienda(descripcion = 'Departamento'),
    TipoVivienda(descripcion = 'Casa'),
    TipoVivienda(descripcion = 'Parcela')
]

TIPO_SERVICIO : list[TipoServicio] = [
    TipoServicio(descripcion = 'TRANSPORTE'),
    TipoServicio(descripcion = 'TOUR')
]

# Vivienda

'''
VIVIENDA : list[Vivienda] = [
    Vivienda(latitud = '-33.5342',longitud = '-70.59299',m2 = '53.45',estrellas = None,id_dis = '1', nombre = 'Gran Avenida', descripcion = 'Departamento amplio, esta es una descripción de prueba',direccion = 'Calle Prueba #123',slug = 'gran-avenida',imagen_principal = None,valor_noche = '50000',abono_base = None,id_ciu = '19111', id_est = '2824',id_pai = '44',capacidad = '3', id_tip = TipoVivienda.objects.get(id = 1), internet = '1', luz = '1' , gas = '1', agua = '1'),
    Vivienda(latitud = '-33.5342',longitud = '-70.59299',m2 = '23.45',estrellas = None,id_dis = '1', nombre = 'Hiper Florida', descripcion = 'Departamento amplio, esta es una descripción de prueba',direccion = 'Calle Prueba #321',slug = 'hiper-florida',imagen_principal = None,valor_noche = '30000',abono_base = None,id_ciu = '19111',id_est = '2824',id_pai = '44',capacidad = '4', id_tip = TipoVivienda.objects.get(id = 1), internet = '1', luz = '1' , gas = '1', agua = '1'),
]
'''

# Diccionario con los modelos de la base de datos
ENTITY = {
    'GENERO' : GENEROS,
    'MODELO' : MODELOS,
    'DOCUMENTOS_IDENTIDAD' : DOCUMENTOS_IDENTIDAD,
    'PRODUCTO' : PRODUCTO,
}

def save_entity(model_name : str):
    for generic in ENTITY[model_name]:
        generic.save()

def run_seed():
    for key in ENTITY.keys():
        print(key)
        save_entity(key)
        



'''


-- PERSONA
Insert into TURISMO_REAL.PERSONA (ID,RUN,DV,PASAPORTE,NOMBRE,SNOMBRE,AP_PATERNO,AP_MATERNO,FECHA_NACIMIENTO,TELEFONO,NUM_CALLE,CALLE,ESTADO,CREACION,ACTUALIZACION,ID_CIU,ID_EST,ID_PAI,ID_DOC,ID_EST1,ID_GEN) values ('1','20281676','2',null,'JORGE','ALEJANDRO','QUINTUI','VERGARA',to_date('02/10/00','DD/MM/RR'),'965928439','1705','Cerro Paranal','ACTIVO',to_timestamp('12/10/22 02:47:13,985533000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 02:47:13,985533000','DD/MM/RR HH24:MI:SSXFF'),'1','1','44','2','1','1');

-- PRODUCTO
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('1','2','Televisor','200000','ACTIVO',to_timestamp('12/10/22 03:01:13,158657000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:01:42,178711000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('2','2','Cocina','80000','ACTIVO',to_timestamp('12/10/22 03:01:38,050599000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:01:38,050599000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('3','2','Refrigerador','100000','ACTIVO',to_timestamp('12/10/22 03:02:08,852450000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:02:08,852450000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('4','1','Ducha','10000','ACTIVO',to_timestamp('12/10/22 03:02:32,588313000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:02:32,588313000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('5','2','Microondas','1000','ACTIVO',to_timestamp('12/10/22 03:02:48,030859000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:02:48,030859000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('7','2','Aspiradora','1000','ACTIVO',to_timestamp('12/10/22 03:03:16,941936000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:03:16,941936000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('8','2','Juguera','10000','ACTIVO',to_timestamp('12/10/22 03:03:30,601626000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:03:30,601626000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('9','2','Tostador','1000','ACTIVO',to_timestamp('12/10/22 03:03:45,078432000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:03:45,078432000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('10','1','Velador','10000','ACTIVO',to_timestamp('12/10/22 03:04:19,665980000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:04:19,665980000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('11','1','Cómoda','10000','ACTIVO',to_timestamp('12/10/22 03:04:31,037375000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:04:31,037375000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('12','1','Clóset','1000','ACTIVO',to_timestamp('12/10/22 03:04:52,377918000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:04:52,377918000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('13','1','Escritorio','10000','ACTIVO',to_timestamp('12/10/22 03:05:06,903702000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:05:06,903702000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('14','1','Armario','10000','ACTIVO',to_timestamp('12/10/22 03:05:23,490968000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:05:23,490968000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('15','1','Estante','10000','ACTIVO',to_timestamp('12/10/22 03:05:38,350791000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:05:38,350791000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('16','1','Sofá','100000','ACTIVO',to_timestamp('12/10/22 03:06:00,931007000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:06:00,931007000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('17','1','Cama Individual','200000','ACTIVO',to_timestamp('12/10/22 03:06:15,462815000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:06:15,462815000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('18','1','Cama 2 plazas','400000','ACTIVO',to_timestamp('12/10/22 03:06:36,365920000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:06:36,365920000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('19','1','Mesa Comedor','100000','ACTIVO',to_timestamp('12/10/22 03:07:02,113528000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:07:02,113528000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('20','3','Secador de pelo','10000','ACTIVO',to_timestamp('12/10/22 03:07:21,571022000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:07:21,571022000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('21','3','Depilador','1','ACTIVO',to_timestamp('12/10/22 03:07:35,069282000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:07:35,069282000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('22','3','Plancha Alisadora','20000','ACTIVO',to_timestamp('12/10/22 03:07:49,379536000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:08:18,148983000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('23','3','Afeitadora','5000','ACTIVO',to_timestamp('12/10/22 03:08:06,654087000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:08:06,654087000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.PRODUCTO (ID,ID_CAT,DESCRIPCION,PRECIO,ESTADO,CREACION,ACTUALIZACION) values ('6','2','Lavadora','10000','ACTIVO',to_timestamp('12/10/22 03:03:02,571675000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 03:03:02,571675000','DD/MM/RR HH24:MI:SSXFF'));

-- MULTA
Insert into TURISMO_REAL.TRAMO_MULTA (ID,ESTADO_PROD,PORCENTAJE,ESTADO,CREACION,ACTUALIZACION) values ('1','1','0','ACTIVO',to_timestamp('11/10/22 23:32:30,000000000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('11/10/22 23:32:30,000000000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.TRAMO_MULTA (ID,ESTADO_PROD,PORCENTAJE,ESTADO,CREACION,ACTUALIZACION) values ('2','2','20','ACTIVO',to_timestamp('11/10/22 23:32:30,006000000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('11/10/22 23:32:30,006000000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.TRAMO_MULTA (ID,ESTADO_PROD,PORCENTAJE,ESTADO,CREACION,ACTUALIZACION) values ('3','3','40','ACTIVO',to_timestamp('11/10/22 23:32:30,012000000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('11/10/22 23:32:30,012000000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.TRAMO_MULTA (ID,ESTADO_PROD,PORCENTAJE,ESTADO,CREACION,ACTUALIZACION) values ('4','4','60','ACTIVO',to_timestamp('11/10/22 23:32:30,018000000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('11/10/22 23:32:30,018000000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.TRAMO_MULTA (ID,ESTADO_PROD,PORCENTAJE,ESTADO,CREACION,ACTUALIZACION) values ('5','5','80','ACTIVO',to_timestamp('11/10/22 23:32:30,023000000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('11/10/22 23:32:30,023000000','DD/MM/RR HH24:MI:SSXFF'));
Insert into TURISMO_REAL.TRAMO_MULTA (ID,ESTADO_PROD,PORCENTAJE,ESTADO,CREACION,ACTUALIZACION) values ('6','6','100','ACTIVO',to_timestamp('11/10/22 23:32:30,028000000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('11/10/22 23:32:30,028000000','DD/MM/RR HH24:MI:SSXFF'));


-- VIVIENDA
Insert into TURISMO_REAL.VIVIENDA (ID,LATITUD,LONGITUD,M2,ESTRELLAS,ID_DIS,NOMBRE,DESCRIPCION,DIRECCION,SLUG,IMAGEN_PRINCIPAL,VALOR_NOCHE,ABONO_BASE,ID_CIU,ID_EST,ID_PAI,CAPACIDAD,INTERNET,ESTADO,AGUA,LUZ,GAS,CREACION,ACTUALIZACION,ID_TIP) values ('1','-33.5342','-70.59299','53.45',null,'1','Gran Avenida','Departamento amplio, esta es una descripción de prueba','Calle Prueba #123','gran-avenida','viviendas/gran-avenida.jpg','50000',null,'19111','2824','44','3','1','ACTIVO','1','1','1',to_timestamp('12/10/22 02:44:12,449614000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 02:44:12,449614000','DD/MM/RR HH24:MI:SSXFF'),'1');
Insert into TURISMO_REAL.VIVIENDA (ID,LATITUD,LONGITUD,M2,ESTRELLAS,ID_DIS,NOMBRE,DESCRIPCION,DIRECCION,SLUG,IMAGEN_PRINCIPAL,VALOR_NOCHE,ABONO_BASE,ID_CIU,ID_EST,ID_PAI,CAPACIDAD,INTERNET,ESTADO,AGUA,LUZ,GAS,CREACION,ACTUALIZACION,ID_TIP) values ('2','-33.5342','-70.59299','23.45',null,'1','Hiper Florida','Departamento amplio, esta es una descripción de prueba','Calle Prueba #321','hiper-florida','viviendas/florida-grand.jpg','30000',null,'19111','2824','44','4','1','ACTIVO','1','1','1',to_timestamp('12/10/22 02:46:25,380484000','DD/MM/RR HH24:MI:SSXFF'),to_timestamp('12/10/22 02:46:25,380484000','DD/MM/RR HH24:MI:SSXFF'),'1');

-- EMPLEADO
Insert into TURISMO_REAL.EMPLEADO (ID,SUELDO,FECHA_CONTRATO,ID_CAR) values ('1','1',to_date('11/10/22','DD/MM/RR'),'2');


'''