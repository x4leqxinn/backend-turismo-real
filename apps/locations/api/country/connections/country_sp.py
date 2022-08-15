# Importamos la librería para conectarnos a la base de datos
from django.db import connections

def listCountry(db_user):
    # La sentencia with se encarga de cerrar la conexión de forma implicita
    with connections[db_user].cursor() as cursor:
        out_cur = connections[db_user].cursor().connection.cursor()
        # Llamado a la base de datos
        cursor.callproc("PKG_COUNTRY.SP_LIST_COUNTRY",[out_cur])
        # Recuparación de la data
        list = []
        for row in out_cur:
            list.append(row)
        return list

def retrieveCountry(db_user,pk):
    with connections[db_user].cursor() as cursor:
        out_cur = connections[db_user].cursor().connection.cursor()
        # Llamado a la base de datos
        cursor.callproc("PKG_COUNTRY.SP_RETRIEVE_COUNTRY",[pk,out_cur])
        # Recuparación de la data
        list = []
        for row in out_cur:
            list.append(row)
        return list