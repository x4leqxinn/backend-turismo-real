from django.contrib import admin
from apps.base.models.db_models import *
from django import forms

'''
class SelectWOA(Select):
    def create_option(self, name, value, label, selected, index, 
                      subindex=None, attrs=None):
        option_dict = super(SelectWOA, self).create_option(name, value, 
            label, selected, index, subindex=subindex, attrs=attrs)
            #Category.objects.
        try:
            option_dict['attrs']['style'] =  'color: ' +  Category.objects.get(name=label).color + ';' 
        except:
            pass
            
        return option_dict

from django.forms import ChoiceField, ModelChoiceField
from category.models import Category

'''

from django.forms import ChoiceField, ModelChoiceField

STATE_CHOICES = (
    ("ACTIVO", "ACTIVO"),
    ("INACTIVO", "INACTIVO"),
)


class MarcaAdminForm(forms.ModelForm):
    estado = ChoiceField(choices=STATE_CHOICES)
    
    class Meta:
        model = Marca
        fields = ('nombre','estado',)


class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','estado')
    ordering = ('id', 'nombre')
    search_fields = ('nombre', 'id','estado')
    list_editable = ('nombre',)
    #list_display_links = ('nombre',)
    list_filter= ('nombre',) 
    list_per_page = 3 # Paginación
    form = MarcaAdminForm

    def get_actions (self,request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions




# Register your models here.
admin.site.register(Genero)
admin.site.register(Sala)
admin.site.register(Cargo)
admin.site.register(Color)
admin.site.register(Modelo)
admin.site.register(Marca,MarcaAdmin)
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