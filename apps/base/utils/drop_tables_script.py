from django.db import connections
from django.utils.connection import ConnectionDoesNotExist
from django.db.utils import DatabaseError

def run_drop_tables(schema_name):
    value = 0
    try:
        with connections[schema_name].cursor() as cursor:
            cursor.callproc("PKG_UTILS.SP_DROP_TABLES")  
        return True, value
    except Exception as ex:
        if(type(ex) is DatabaseError):
            value = 2
        if(type(ex) is ConnectionDoesNotExist):
            value = 1
        return False, value