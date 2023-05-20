from django.contrib import admin

# Register your models here.
from .models import Edificio, UnidadFuncional, Amenity, ReservaAmeni

class EdificioAdmin (admin.ModelAdmin):
        # Campos a mostrar en la lista de registros del modelo
        list_display = ['provincia', 'ciudad', 'direccion']

        # Campos que se utilizarán para realizar búsquedas
        search_fields = ['provincia', 'ciudad', 'direccion']

        # Filtros que se mostrarán en el panel lateral
        list_filter = ['provincia', 'ciudad', 'direccion']

        # Campos que se mostrarán en el formulario de edición (Alta/Modificación)
        fields = ['provincia','ciudad', 'direccion']    
	
        # Define el número de elementos por página
        list_per_page = 10
        
class UnidadFuncionalAdmin (admin.ModelAdmin):
        pass
class AmenityAdmin(admin.ModelAdmin):
        pass
class ReservaAmenityAdmin(admin.ModelAdmin):
        pass
    
admin.site.register(Edificio, EdificioAdmin)
admin.site.register(UnidadFuncional, UnidadFuncionalAdmin)
admin.site.register(Amenity, AmenityAdmin)
admin.site.register(ReservaAmeni, ReservaAmenityAdmin)

