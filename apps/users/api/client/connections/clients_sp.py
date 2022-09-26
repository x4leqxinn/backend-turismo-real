# Importamos la librería para conectarnos a la base de datos
from django.db import connections

from apps.users.api.client.models.models import Client

def listClient(db_user):
    # La sentencia with se encarga de cerrar la conexión de forma implicita
    with connections[db_user].cursor() as cursor:
        out_cur = connections[db_user].cursor().connection.cursor()
        # Llamado a la base de datos
        cursor.callproc("SP_CLIENT_LIST",[out_cur])
        # Recuparación de la data
        list = []
        for row in out_cur:
            list.append(row)
        return list
        


def retrieveClient(db_user,pk):
    pass


def createClient(db_user,client : Client):
    from datetime import datetime
    # La sentencia with se encarga de cerrar la conexión de forma implicita
    with connections[db_user].cursor() as cursor:
        
        # CONSUMIR VARIABLES
        outval = cursor.var(int).var
        #('42534543','2',null,'Jorge','Alejandro','Quintui','Vergara',to_date('02/10/2000'),'65928439','1384','Monas Xinas Crew',1,1,1,1,1,2,:b_out_num)
        # llamado
        cursor.callproc("PKG_CLIENT.SP_CREATE_CLIENT",[
            client.rut,
            client.dv,
            client.pasaporte,
            client.nombre,
            client.snombre,
            client.ap_paterno,
            client.ap_materno,
            datetime.strptime(client.fecha_nacimiento, '%d/%m/%Y'),
            client.telefono,
            client.num_calle,
            client.calle,
            client.id_ciu,
            client.id_est,
            client.id_pai,
            client.id_doc,
            client.id_est_civ,
            client.id_gen,
            outval
        ])
        print(outval.getvalue())        
    return outval.getvalue()




'''

-- EXECUTE PKG_CLIENT.SP_CREATE_CLIENT('42534543','2',null,'Jorge','Alejandro','Quintui','Vergara',to_date('02/10/2000'),'65928439','1384','Monas Xinas Crew',1,1,1,1,1,2,:b_out_num);


-- EXECUTE PKG_CLIENT.SP_UPDATE_CLIENT(1,'20281676','2',null,'Jorge','Alejandro','Quintui','Vergara',SYSDATE,'65928439','1384','Monas Xinas Crew',1,1,1,1,1,2,:b_out_num);

-- EXECUTE PKG_CLIENT.SP_DELETE_CLIENT(1,:b_out_num);

'''