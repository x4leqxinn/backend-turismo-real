from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# Se definen las credenciales de las bases de datos
DATABASES = {
    'default' : {},
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
    }
}

# Se definen los enrutadores para el acceso a las bases de datos
DATABASE_ROUTERS = [
    'db_routers.turismo_real_router.TurismoRealRouter',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Indicamos donde serviremos nuestras imágenes
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'../media')

