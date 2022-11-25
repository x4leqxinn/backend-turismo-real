from django.db import connections
from django.utils.connection import ConnectionDoesNotExist
from django.db.utils import DatabaseError
import environ
env = environ.Env()
environ.Env.read_env(env_file='./.env') 

def run_create_schema():
    user = 'CREATE USER {} IDENTIFIED BY "{}"'.format(env.str('DATABASE_USER_1'),env.str('DATABASE_PASSWORD_1'))
    permissions = 'GRANT CONNECT, RESOURCE, DBA TO {}'.format(env.str('DATABASE_USER_1'))
    try:
        with connections['system'].cursor() as cursor:
            cursor.execute('ALTER SESSION SET "_oracle_script"=true')
            cursor.execute(user)
            cursor.execute(permissions)
    except Exception as ex:
        pass