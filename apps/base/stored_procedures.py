# Importamos la librería para conectarnos a la base de datos
from django.db import connections

def genericDelete(db_user : str, pk : int, model_name : str):
    with connections[db_user].cursor() as cursor:
        outval = cursor.var(int).var
        cursor.callproc("PKG_UTILS.SP_DELETE_ENTITY",[pk,model_name,outval])        
    return outval.getvalue()