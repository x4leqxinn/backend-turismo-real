from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# Se definen las credenciales de las bases de datos
DATABASES = {
    'default' : {
        'ENGINE': env.str('DATABASE_ENGINE_1'),
        'NAME': env.str('DATABASE_NAME_1'),
        'USER': env.str('DATABASE_USER_1'),
        'PASSWORD' : env.str('DATABASE_PASSWORD_1'),
        'TEST' : {
            'USER' : env.str('DATABASE_TEST_USER_1'),
            'TBLSPACE' : env.str('DATABASE_TBLSPACE_1'),
            'TBLSPACE_TMP' : env.str('DATABASE_TBLSPACE_TMP_1')
        }
    },
    # System connection
    'system': {
        'ENGINE': env.str('DATABASE_ENGINE_3'),
        'NAME': env.str('DATABASE_NAME_3'),
        'USER': env.str('DATABASE_USER_3'),
        'PASSWORD' : env.str('DATABASE_PASSWORD_3'),
        'TEST' : {
            'USER' : env.str('DATABASE_TEST_USER_3'),
            'TBLSPACE' : env.str('DATABASE_TBLSPACE_3'),
            'TBLSPACE_TMP' : env.str('DATABASE_TBLSPACE_TMP_3')
        }
    },
    # ORACLE Turismo Real API
    'turismo_real': {
        'ENGINE': env.str('DATABASE_ENGINE_1'),
        'NAME': env.str('DATABASE_NAME_1'),
        'USER': env.str('DATABASE_USER_1'),
        'PASSWORD' : env.str('DATABASE_PASSWORD_1'),
        'TEST' : {
            'USER' : env.str('DATABASE_TEST_USER_1'),
            'TBLSPACE' : env.str('DATABASE_TBLSPACE_1'),
            'TBLSPACE_TMP' : env.str('DATABASE_TBLSPACE_TMP_1')
        }
    },
    # MYSQL API 
    'country_api' : {
        'ENGINE': env.str('DATABASE_ENGINE_2'),  
        'NAME': env.str('DATABASE_NAME_2'),  
        'USER': env.str('DATABASE_USER_2'),  
        'PASSWORD': env.str('DATABASE_PASSWORD_2'),  
        'HOST': env.str('DATABASE_HOST_2'),  
        'PORT': env.str('DATABASE_PORT_2'),  
        'OPTIONS': {  
            'init_command': env.str('DATABASE_INIT_2')  
        }  
    }    
}

# Se definen los enrutadores para el acceso a las bases de datos
DATABASE_ROUTERS = [
    'db_routers.country_api_router.CountryApiRouter',
    'db_routers.turismo_real_router.TurismoRealRouter',
    'db_routers.system_router.SystemRouter',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Indicamos donde serviremos nuestras imágenes
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'../media')

