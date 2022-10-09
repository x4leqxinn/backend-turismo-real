from django.contrib import admin
from apps.locations.models import *
from django import forms

# Register your models here.


# Countries Admin
class CountriesAdminForm(forms.ModelForm):

    class Meta:
        model = Countries
        fields = ('__all__')

class CountriesAdmin(admin.ModelAdmin):
    list_display = ('id','name','iso3','currency','region','native')
    ordering = ('id','name','iso3','currency','region')
    search_fields = ('id','name','iso3','currency','region','phonecode','capital','tld','native','subregion')
    list_display_links = ('id','name','iso3','currency','region','native')
    list_filter= ('id','name','iso3','currency','region','phonecode','capital','tld','native','subregion') 
    list_per_page = 10
    form = CountriesAdminForm

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Countries,CountriesAdmin)


# States Admin
class StatesAdminForm(forms.ModelForm):

    class Meta:
        model = States
        fields = ('__all__')

class StatesAdmin(admin.ModelAdmin):
    list_display = ('id','name','country_code','iso2')
    ordering = ('id','name','country_code','iso2')
    search_fields = ('id','name','country_code','iso2')
    list_display_links = ('id','name','country_code','iso2')
    list_filter= ('id','name','country_code','iso2','country_id') 
    list_per_page = 10
    form = StatesAdminForm

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(States,StatesAdmin)

class CitiesAdminForm(forms.ModelForm):

    class Meta:
        model = Cities
        fields = ('__all__')
class CitiesAdmin(admin.ModelAdmin):
    list_display = ('id','name','state_code','country_code')
    ordering = ('id','name','state_code','country_code')
    search_fields = ('id','name','state_code','country_code')
    list_display_links = ('id','name','state_code','country_code')
    list_filter= ('id','name','state_code','country_code','country_id','state_id') 
    list_per_page = 10
    form = CitiesAdminForm

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Cities,CitiesAdmin)

