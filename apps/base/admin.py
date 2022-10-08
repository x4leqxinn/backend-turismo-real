from django.contrib import admin
from apps.base.models.db_models import *
from django import forms
from django.forms import ChoiceField

STATE_CHOICES = (
    ("ACTIVO", "ACTIVO"),
    ("INACTIVO", "INACTIVO"),
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

admin.site.register(Modelo)
admin.site.register(Disponibilidad)
admin.site.register(EstadoCivil)
admin.site.register(DocIdentidad)
admin.site.register(TipoDocumento)
admin.site.register(TipoVivienda)
admin.site.register(TipoServicio)
admin.site.register(EstadoProducto)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Vivienda)
admin.site.register(Inventario)
admin.site.register(DetalleSala)
admin.site.register(DetalleProducto)
admin.site.register(Persona)
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Recepcionista)
admin.site.register(Conductor)
admin.site.register(GaleriaInterior)
admin.site.register(GaleriaExterior)
admin.site.register(CliCom)
admin.site.register(Comentario)