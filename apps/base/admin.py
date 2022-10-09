from django.contrib import admin
from apps.base.models.db_models import *
from django import forms
from django.forms import ChoiceField

STATE_CHOICES = (
    ("ACTIVO", "ACTIVO"),
    ("INACTIVO", "INACTIVO"),
)

DWELLING_CHOICES = (
    (0, "No"),
    (1, "Sí"),
)

# Marca Admin
class MarcaAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = Marca
        fields = ('nombre','estado',)
class MarcaAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','nombre','estado')
    ordering = ('id', 'nombre')
    search_fields = ('nombre', 'id','estado')
    list_editable = ('nombre',)
    list_display_links = ('id',)
    list_filter= ('nombre','estado') 
    list_per_page = 5
    form = MarcaAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for marca in queryset:
            marca.estado = 'ACTIVO'
            marca.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for marca in queryset:
            marca.estado = 'INACTIVO'
            marca.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Marca,MarcaAdmin)

# Genero Admin
class GeneroAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = Genero
        fields = ('descripcion','estado',)
class GeneroAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','descripcion','estado')
    ordering = ('id', 'descripcion')
    search_fields = ('descripcion', 'id','estado')
    list_editable = ('descripcion',)
    list_display_links = ('id',)
    list_filter= ('descripcion','estado') 
    list_per_page = 5
    form = GeneroAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for genero in queryset:
            genero.estado = 'ACTIVO'
            genero.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for genero in queryset:
            genero.estado = 'INACTIVO'
            genero.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Genero,GeneroAdmin)


# Sala Admin
class SalaAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = Sala
        fields = ('descripcion','estado',)
class SalaAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','descripcion','estado')
    ordering = ('id', 'descripcion')
    search_fields = ('descripcion', 'id','estado')
    list_editable = ('descripcion',)
    list_display_links = ('id',)
    list_filter= ('descripcion','estado') 
    list_per_page = 5
    form = SalaAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for sala in queryset:
            sala.estado = 'ACTIVO'
            sala.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for sala in queryset:
            sala.estado = 'INACTIVO'
            sala.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Sala,SalaAdmin)

# Cargo Admin
class CargoAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = Cargo
        fields = ('descripcion','estado',)

class CargoAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','descripcion','estado')
    ordering = ('id', 'descripcion')
    search_fields = ('descripcion', 'id','estado')
    list_editable = ('descripcion',)
    list_display_links = ('id',)
    list_filter= ('descripcion','estado') 
    list_per_page = 5
    form = CargoAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for cargo in queryset:
            cargo.estado = 'ACTIVO'
            cargo.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for cargo in queryset:
            cargo.estado = 'INACTIVO'
            cargo.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Cargo,CargoAdmin)

# Color Admin
class ColorAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = Color
        fields = ('nombre','estado',)

class ColorAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','nombre','estado')
    ordering = ('id', 'nombre')
    search_fields = ('nombre', 'id','estado')
    list_editable = ('nombre',)
    list_display_links = ('id',)
    list_filter= ('nombre','estado') 
    list_per_page = 5
    form = ColorAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for color in queryset:
            color.estado = 'ACTIVO'
            color.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for color in queryset:
            color.estado = 'INACTIVO'
            color.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Color,ColorAdmin)

# Modelo Admin
class ModeloAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = Modelo
        fields = ('nombre','estado',)

class ModeloAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','nombre','estado')
    ordering = ('id', 'nombre')
    search_fields = ('nombre', 'id','estado')
    list_editable = ('nombre',)
    list_display_links = ('id',)
    list_filter= ('nombre','estado') 
    list_per_page = 5
    form = ModeloAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for Modelo in queryset:
            Modelo.estado = 'ACTIVO'
            Modelo.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for Modelo in queryset:
            Modelo.estado = 'INACTIVO'
            Modelo.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Modelo,ModeloAdmin)

# Disponibilidad Admin
class DisponibilidadAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = Disponibilidad
        fields = ('estado',)

class DisponibilidadAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','descripcion','estado')
    ordering = ('id', 'descripcion')
    search_fields = ('descripcion', 'id','estado')
    list_display_links = ('id',)
    list_filter= ('descripcion','estado') 
    list_per_page = 5
    form = DisponibilidadAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for disponibilidad in queryset:
            disponibilidad.estado = 'ACTIVO'
            disponibilidad.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for disponibilidad in queryset:
            disponibilidad.estado = 'INACTIVO'
            disponibilidad.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(Disponibilidad,DisponibilidadAdmin)

# EstadoCivil Admin
class EstadoCivilAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = EstadoCivil
        fields = ('descripcion','estado',)

class EstadoCivilAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','descripcion','estado')
    ordering = ('id', 'descripcion')
    search_fields = ('descripcion', 'id','estado')
    list_editable = ('descripcion',)
    list_display_links = ('id',)
    list_filter= ('descripcion','estado') 
    list_per_page = 5
    form = EstadoCivilAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for estadoCivil in queryset:
            estadoCivil.estado = 'ACTIVO'
            estadoCivil.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for estadoCivil in queryset:
            estadoCivil.estado = 'INACTIVO'
            estadoCivil.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(EstadoCivil,EstadoCivilAdmin)

# DocIdentidad Admin
class DocIdentidadAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = DocIdentidad
        fields = ('descripcion','estado',)

class DocIdentidadAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','descripcion','estado')
    ordering = ('id', 'descripcion')
    search_fields = ('descripcion', 'id','estado')
    list_editable = ('descripcion',)
    list_display_links = ('id',)
    list_filter= ('descripcion','estado') 
    list_per_page = 5
    form = DocIdentidadAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for docIdentidad in queryset:
            docIdentidad.estado = 'ACTIVO'
            docIdentidad.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for docIdentidad in queryset:
            docIdentidad.estado = 'INACTIVO'
            docIdentidad.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(DocIdentidad,DocIdentidadAdmin)

# TipoDocumento Admin
class TipoDocumentoAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = TipoDocumento
        fields = ('descripcion','estado',)

class TipoDocumentoAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','descripcion','estado')
    ordering = ('id', 'descripcion')
    search_fields = ('descripcion', 'id','estado')
    list_editable = ('descripcion',)
    list_display_links = ('id',)
    list_filter= ('descripcion','estado') 
    list_per_page = 5
    form = TipoDocumentoAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for tipoDocumento in queryset:
            tipoDocumento.estado = 'ACTIVO'
            tipoDocumento.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for tipoDocumento in queryset:
            tipoDocumento.estado = 'INACTIVO'
            tipoDocumento.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(TipoDocumento,TipoDocumentoAdmin)

# TipoVivienda Admin
class TipoViviendaAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = TipoVivienda
        fields = ('descripcion','estado',)

class TipoViviendaAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','descripcion','estado')
    ordering = ('id', 'descripcion')
    search_fields = ('descripcion', 'id','estado')
    list_editable = ('descripcion',)
    list_display_links = ('id',)
    list_filter= ('descripcion','estado') 
    list_per_page = 5
    form = TipoViviendaAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for tipoVivienda in queryset:
            tipoVivienda.estado = 'ACTIVO'
            tipoVivienda.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for tipoVivienda in queryset:
            tipoVivienda.estado = 'INACTIVO'
            tipoVivienda.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(TipoVivienda,TipoViviendaAdmin)

# TipoServicio Admin
class TipoServicioAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = TipoServicio
        fields = ('descripcion','estado',)

class TipoServicioAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','descripcion','estado')
    ordering = ('id', 'descripcion')
    search_fields = ('descripcion', 'id','estado')
    list_editable = ('descripcion',)
    list_display_links = ('id',)
    list_filter= ('descripcion','estado') 
    list_per_page = 5
    form = TipoServicioAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for tipoServicio in queryset:
            tipoServicio.estado = 'ACTIVO'
            tipoServicio.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for tipoServicio in queryset:
            tipoServicio.estado = 'INACTIVO'
            tipoServicio.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(TipoServicio,TipoServicioAdmin)

# EstadoProducto Admin
class EstadoProductoAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = EstadoProducto
        fields = ('descripcion','estado',)

class EstadoProductoAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','descripcion','estado')
    ordering = ('id', 'descripcion')
    search_fields = ('descripcion', 'id','estado')
    list_editable = ('descripcion',)
    list_display_links = ('id',)
    list_filter= ('descripcion','estado') 
    list_per_page = 5
    form = EstadoProductoAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for estadoProducto in queryset:
            estadoProducto.estado = 'ACTIVO'
            estadoProducto.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for estadoProducto in queryset:
            estadoProducto.estado = 'INACTIVO'
            estadoProducto.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(EstadoProducto,EstadoProductoAdmin)


# Producto Admin
class ProductoAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = Producto
        fields = ('descripcion','precio','id_cat','estado')

class ProductoAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','descripcion','precio','id_cat','estado')
    ordering = ('id', 'descripcion','precio')
    search_fields = ('precio','descripcion','id_cat__descripcion', 'id','estado')
    list_editable = ('descripcion','precio','id_cat')
    list_display_links = ('id',)
    list_filter= ('descripcion','precio','id_cat','estado') 
    list_per_page = 5
    form = ProductoAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for producto in queryset:
            producto.estado = 'ACTIVO'
            producto.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for producto in queryset:
            producto.estado = 'INACTIVO'
            producto.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Producto,ProductoAdmin)

# Categoria Admin
class CategoriaAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = Categoria
        fields = ('descripcion','estado',)

class CategoriaAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','descripcion','estado')
    ordering = ('id', 'descripcion')
    search_fields = ('descripcion', 'id','estado')
    list_editable = ('descripcion',)
    list_display_links = ('id',)
    list_filter= ('descripcion','estado') 
    list_per_page = 5
    form = CategoriaAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for categoria in queryset:
            categoria.estado = 'ACTIVO'
            categoria.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for categoria in queryset:
            categoria.estado = 'INACTIVO'
            categoria.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Categoria,CategoriaAdmin)

# Vivienda Admin
class ViviendaAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    internet = ChoiceField(choices=DWELLING_CHOICES)
    luz = ChoiceField(choices=DWELLING_CHOICES)
    gas = ChoiceField(choices=DWELLING_CHOICES)
    agua = ChoiceField(choices=DWELLING_CHOICES)
    class Meta:
        model = Vivienda
        exclude = ('creacion','actualizacion','id', 'estrellas','abono_base')

class ViviendaAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','nombre','descripcion','estado')
    ordering = ('id', 'descripcion','direccion','nombre')
    search_fields = ('descripcion', 'id','direccion','estado','nombre')
    list_editable = ('descripcion','nombre')
    list_display_links = ('id',)
    list_filter= ('descripcion','estado','nombre','id_pai','id_ciu','id_est') 
    list_per_page = 5
    form = ViviendaAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for vivienda in queryset:
            vivienda.estado = 'ACTIVO'
            vivienda.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for vivienda in queryset:
            vivienda.estado = 'INACTIVO'
            vivienda.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Vivienda,ViviendaAdmin)

# Empleado Admin
class EmpleadoAdminForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ('__all__')

class EmpleadoAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','sueldo','fecha_contrato','id_car')
    ordering = ('id','sueldo')
    search_fields = ('id','fecha_contrato','sueldo')
    list_editable = ('sueldo',)
    list_display_links = ('id',)
    list_filter= ('sueldo','id','fecha_contrato') 
    list_per_page = 5
    form = EmpleadoAdminForm

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Empleado,EmpleadoAdmin)

# Recepcionista Admin
class RecepcionistaAdminForm(forms.ModelForm):
    class Meta:
        model = Recepcionista
        fields = ('__all__')

class RecepcionistaAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id',)
    ordering = ('id',)
    search_fields = ('id',)
    #list_editable = ('sueldo',)
    list_display_links = ('id',)
    list_filter= ('id',) 
    list_per_page = 5
    form = RecepcionistaAdminForm

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Recepcionista,RecepcionistaAdmin)

# Conductor Admin
class ConductorAdminForm(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = ('__all__')

class ConductorAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id',)
    ordering = ('id',)
    search_fields = ('id',)
    #list_editable = ('sueldo',)
    list_display_links = ('id',)
    list_filter= ('id',) 
    list_per_page = 5
    form = ConductorAdminForm

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Conductor,ConductorAdmin)

# Persona Admin
class PersonaAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = Persona
        fields = ('__all__')

class PersonaAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','nombre','ap_paterno','ap_materno','fecha_nacimiento','estado')
    ordering = ('id', 'nombre')
    search_fields = ('nombre', 'id','estado')
    list_display_links = ('id',)
    list_filter= ('nombre','ap_paterno','ap_materno','estado','id_ciu','id_pai','id_est') 
    list_per_page = 5
    form = PersonaAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for persona in queryset:
            persona.estado = 'ACTIVO'
            persona.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for persona in queryset:
            persona.estado = 'INACTIVO'
            persona.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Persona,PersonaAdmin)

# Cliente Admin
class ClienteAdminForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('__all__')

class ClienteAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id',)
    ordering = ('id',)
    search_fields = ('id',)
    #list_editable = ('sueldo',)
    list_display_links = ('id',)
    list_filter= ('id',) 
    list_per_page = 5
    form = ClienteAdminForm

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Cliente,ClienteAdmin)

# Inventario Admin
class InventarioAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = Inventario
        fields = ('id_viv','estado',)

class InventarioAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','id_viv','estado')
    ordering = ('id', 'id_viv')
    search_fields = ('id_viv', 'id','estado')
    list_display_links = ('id',)
    list_filter= ('id_viv','estado') 
    list_per_page = 5
    form = InventarioAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for inventario in queryset:
            inventario.estado = 'ACTIVO'
            inventario.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for inventario in queryset:
            inventario.estado = 'INACTIVO'
            inventario.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Inventario,InventarioAdmin)

class GaleriaInteriorAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = GaleriaInterior
        fields = ('__all__')
class GaleriaInteriorAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','imagen','id_viv','estado')
    ordering = ('id', 'imagen','id_viv')
    search_fields = ('imagen', 'id','estado')
    list_editable = ('imagen',)
    list_display_links = ('id','id_viv')
    list_filter= ('estado','id_viv','id') 
    list_per_page = 5
    form = GaleriaInteriorAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for galeriaInterior in queryset:
            galeriaInterior.estado = 'ACTIVO'
            galeriaInterior.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for galeriaInterior in queryset:
            galeriaInterior.estado = 'INACTIVO'
            galeriaInterior.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(GaleriaInterior,GaleriaInteriorAdmin)


# GaleriaExterior Admin
class GaleriaExteriorAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = GaleriaExterior
        fields = ('__all__')

class GaleriaExteriorAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','imagen','id_viv','estado')
    ordering = ('id', 'imagen','id_viv')
    search_fields = ('imagen', 'id','estado')
    list_editable = ('imagen',)
    list_display_links = ('id','id_viv')
    list_filter= ('estado','id_viv','id') 
    list_per_page = 5
    form = GaleriaExteriorAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for galeriaExterior in queryset:
            galeriaExterior.estado = 'ACTIVO'
            galeriaExterior.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for galeriaExterior in queryset:
            galeriaExterior.estado = 'INACTIVO'
            galeriaExterior.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(GaleriaExterior,GaleriaExteriorAdmin)


# CliCom Admin
class CliComAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = CliCom
        fields = ('estado',)

class CliComAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','id_cli','id_viv','estado')
    ordering = ('id', 'id_cli','id_viv')
    search_fields = ('id_cli','id_viv', 'id','estado')
    list_display_links = ('id','id_cli','id_viv')
    list_filter= ('id_cli','id_viv','estado') 
    list_per_page = 5
    form = CliComAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for cliCom in queryset:
            cliCom.estado = 'ACTIVO'
            cliCom.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for cliCom in queryset:
            cliCom.estado = 'INACTIVO'
            cliCom.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(CliCom,CliComAdmin)


# Comentario Admin
class ComentarioAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = Comentario
        fields = ('estado',)

class ComentarioAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','descripcion','id_cli','estado')
    ordering = ('id', 'descripcion')
    search_fields = ('descripcion', 'id','estado')
    list_display_links = ('id','descripcion')
    list_filter= ('descripcion','estado','id') 
    list_per_page = 5
    form = ComentarioAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for comentario in queryset:
            comentario.estado = 'ACTIVO'
            comentario.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for comentario in queryset:
            comentario.estado = 'INACTIVO'
            comentario.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(Comentario,ComentarioAdmin)

# DetalleSala Admin

class DetalleSalaAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = DetalleSala
        fields = ('__all__')

class DetalleSalaAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','imagen_sala','id_sal','id_inv','estado')
    ordering = ('id', )
    search_fields = ('id','estado')
    list_display_links = ('id',)
    list_editable = ('imagen_sala',)
    list_filter= ('estado','id','id_sal') 
    list_per_page = 5
    form = DetalleSalaAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for detalleSala in queryset:
            detalleSala.estado = 'ACTIVO'
            detalleSala.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for detalleSala in queryset:
            detalleSala.estado = 'INACTIVO'
            detalleSala.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(DetalleSala,DetalleSalaAdmin)


# DetalleProducto Admin

class DetalleProductoAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = DetalleProducto
        fields = ('__all__')

class DetalleProductoAdmin(admin.ModelAdmin):
    actions = ['active_state','inactive_state']
    list_display = ('id','id_pro','id_det','id_est','estado')
    ordering = ('id', )
    search_fields = ('id','estado')
    list_display_links = ('id','id_est','id_pro','id_det')
    list_filter= ('estado','id','id_est','id_pro','id_det') 
    list_per_page = 5
    form = DetalleProductoAdminForm

    @admin.action(description='Cambiar estado ACTIVO')
    def active_state(self,request,queryset):
        for detalleProducto in queryset:
            detalleProducto.estado = 'ACTIVO'
            detalleProducto.save()
    
    @admin.action(description='Cambiar estado INACTIVO')
    def inactive_state(self,request,queryset):
        for detalleProducto in queryset:
            detalleProducto.estado = 'INACTIVO'
            detalleProducto.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False
        
admin.site.register(DetalleProducto,DetalleProductoAdmin)


# TODO: Falta personalizar estos modelos
admin.site.register(Reserva)

admin.site.register(DetalleServicio)

admin.site.register(Servicio)

admin.site.register(Movilizacion)
admin.site.register(Transporte)
admin.site.register(Tour)
admin.site.register(DetalleTour)
admin.site.register(Destino)
admin.site.register(Vehiculo)
admin.site.register(DetVehMov)
admin.site.register(DetServMov)
admin.site.register(CheckIn)
admin.site.register(CheckOut)
admin.site.register(DetalleMulta)
admin.site.register(Multa)
admin.site.register(TipoMulta)
admin.site.register(Documento)
admin.site.register(DCheck)
admin.site.register(Registro)
admin.site.register(Salida)
admin.site.register(DCoordinacion)


# TODO: Se pueden agregar modelos de base de datos para modificar la vista de la web dinámicamente