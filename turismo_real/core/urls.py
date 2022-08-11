from django.contrib import admin
from django.urls import path,include,re_path

# Configs para servir las imágenes
from django.conf import settings
from django.conf.urls.static import static

# Configuramos Open API 
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi 

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

urlpatterns = [
    # Open API
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Administración de Django
    path('admin/', admin.site.urls),
]


# Indicamos donde serviremos las imagenes en estado DEBUG
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

