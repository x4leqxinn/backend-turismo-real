from django.contrib import admin
from apps.base.models.db_models import Producto, Categoria, SubCategoria

# Register your models here.

admin.site.register(Producto);
admin.site.register(Categoria);
admin.site.register(SubCategoria);