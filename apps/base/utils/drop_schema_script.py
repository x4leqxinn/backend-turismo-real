from django.db import connections
import environ
env = environ.Env()
environ.Env.read_env(env_file='./.env') 

def run_drop_schema():
    user = 'DROP USER {} CASCADE'.format(env.str('DATABASE_USER_1'))
    try:
        with connections['system'].cursor() as cursor:
            cursor.execute('ALTER SESSION SET "_oracle_script"=true')
            cursor.execute(user)
    except Exception as ex:
        pass