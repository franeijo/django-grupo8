from django.contrib import admin

# Register your models here.
from .models import Edificio, UnidadFuncional, Amenity
from .models import ReservaAmeni, ReclamoSugerencia, Gasto


class EdificioAdmin (admin.ModelAdmin):
    # Campos a mostrar en la lista de registros del modelo
        list_display = ['nombre', 'direccion', 'ciudad']

    # Campos que se utilizarán para realizar búsquedas
        search_fields = ['nombre', 'direccion', 'ciudad']

    # Filtros que se mostrarán en el panel lateral
        list_filter = ['ciudad', 'direccion']

    # Campos que se mostrarán en el formulario de edición (Alta/Modificación)
        fields = ['pais','pcia','ciudad','nombre', 'direccion']    
        
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

