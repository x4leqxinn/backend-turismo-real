from django.contrib import admin
from apps.locations.models import *

# Register your models here.

admin.site.register(Pais)
admin.site.register(EstadoPais)
admin.site.register(Ciudad)

