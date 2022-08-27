from django.contrib import admin
from django.urls import path,include,re_path

# Configs para servir las imágenes
from django.conf import settings
from django.conf.urls.static import static

# Configuramos Open API 
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi 

from apps.users.auth.auth_views import *

schema_view = get_schema_view(
  openapi.Info(
    title='Documentación de API "Turismo Real"',
    default_version='v0.1',
    description="Documentación pública de la API Turismo Real.",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="turismo.real.servicios@gmail.com"),
    license=openapi.License(name="licencia de mona xina"),
  ),
  public=True,
  permission_classes=(permissions.AllowAny,),
)


# TODO: Cambiar la ruta catch all y eliminar el template de prueba de mails

# ELIMINAR DESPUÉS
from templates.views import index

urlpatterns = [
    # Documentación Open API
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # Administración de Django
    path('admin/', admin.site.urls),
    
    # Autenticación de usuarios
    path('logout/', Logout.as_view(),name='logout'),
    path('login/',Login.as_view(),name='login'),
    path('refresh-token/',UserToken.as_view(), name = 'refresh_token'),
    
    # Enrutador de clientes
    #path('admin-api/',include('apps.users.api.routers')), 
    #path('office-api/',include('apps.users.api.routers')),
    path('client-api/',include('apps.users.api.routers')),
    # Enrutador para Países
    path('location-api/',include('apps.locations.api.urls')),

    # Ruta de redirección por url erronéa
    # Momentareamente está la página de envio de mails
    re_path(r'^.*/$', index, name='unmatched'),
]


# Indicamos donde serviremos las imagenes en estado DEBUG
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

