from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuramos la lectura de nuestras variables de entorno
import environ
env = environ.Env()
environ.Env.read_env(env_file='./.env') 


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DJANGO_DEBUG',default=False)

ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS', default=[]))


# Application definition

# Apps por defecto de django 
BASE_APPS = [
    'admin_interface', # Customización del Admin de Django
    'colorfield', # Customización del Admin de Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Apps propias
LOCAL_APPS = [
    'apps.users',
    'apps.locations',
    'apps.people',
    'apps.deptos',
    'apps.base'
]

# Apps de terceros
THIRD_APPS = [
    'corsheaders', # Para habilitar la politica de cors
    'rest_framework',  
    'drf_yasg', # Auto documentar nuestra API
    'rest_framework.authtoken', # Tokens de Autenticación
    'naomi', # Para permitir guardar archivos temporales de mails
    'django_filters', # Registramos los filtros
]

# Asignación de la APPS del aplicativo
INSTALLED_APPS =  BASE_APPS + LOCAL_APPS + THIRD_APPS 


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Definimos mi modelo de usuario CUSTOM
AUTH_USER_MODEL = 'users.User'

# Se define el tiempo de expiración del token a 15 minutos
TOKEN_EXPIRED_AFTER_SECONDS = 900

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True


# Indicamos las conexiones permitidas en la politica de CORS
CORS_ALLOW_HEADERS = [
    '*'
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT"
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True


REST_FRAMEWORK = {
    # Defino los filtros de la app por defecto como globales.
    'DEFAULT_FILTER_BACKENDS' : ('django_filters.rest_framework.DjangoFilterBackend',
    'rest_framework.filters.SearchFilter','rest_framework.filters.OrderingFilter'),
    'SEARCH_PARAM' : 'q', # Cambiamos el parametro de busqueda para para los filtros search
    'ORDERING_PARAM': 'order',
    'DEFAULT_PAGINATION_CLASS' : 'core.pagination.CustomPageNumberPagination', # Definimos la paginación
    'PAGE_SIZE' : 1,
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, '../static'),)

EMAIL_HOST = env.str('EMAIL_HOST')
EMAIL_PORT = env.str('EMAIL_PORT')
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = env.str('EMAIL_USE_TLS')


# Permite verificar los Mails sin enviarlos a usuarios.
if DEBUG:
    EMAIL_BACKEND = "naomi.mail.backends.naomi.NaomiBackend"
    EMAIL_FILE_PATH = os.path.join(BASE_DIR,'../tmp')


# Indicamos donde serviremos nuestras imágenes
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'../media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de SWAGGER autodocumentación de API 
SWAGGER_SETTINGS = {
    'DOC_EXPANSION' : 'none'
}
