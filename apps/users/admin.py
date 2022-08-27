from django.contrib import admin
from apps.users.models import User, UserRole
from apps.users.api.client.models.db_models import Persona, Cliente, Empleado, Recepcionista, Conductor, Cargo

admin.site.register(User)
admin.site.register(UserRole)

admin.site.register(Persona)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Recepcionista)
admin.site.register(Conductor)

admin.site.register(Cargo)

