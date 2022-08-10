from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# Se definen las credenciales de las bases de datos
DATABASES = {
    'default' : {},
    'turismo_real': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '127.0.0.1:1521/orcl',
        'USER': 'turismo_real',
        'PASSWORD' : 'dGz?SfRdC?Y5Bsx?',
        'TEST' : {
            'USER' : 'default_test_tbls',
            'TBLSPACE' : 'default_test_tbls',
            'TBLSPACE_TMP' : 'default_test_tbls_tmp'
        }
    }
}

# Se definen los enrutadores para el acceso a las bases de datos
DATABASE_ROUTERS = [
    'db_routers.turismo_real_router.TurismoRealRouter',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'


