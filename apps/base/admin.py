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