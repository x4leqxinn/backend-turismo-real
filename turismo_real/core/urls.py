from django.contrib import admin
from django.urls import path

# Configs para servir las imágenes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]


# Indicamos donde serviremos las imagenes en estado DEBUG
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

