# Importamos la librería para conectarnos a la base de datos
from django.db import connections

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


def createClient(db_user,client):
    # La sentencia with se encarga de cerrar la conexión de forma implicita
    with connections[db_user].cursor() as cursor:
        
        # CONSUMIR VARIABLES
        outval = cursor.var(int).var
    
        print(outval.getvalue())        
    pass