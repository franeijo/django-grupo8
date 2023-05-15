from django.contrib import admin

# Register your models here.
from .models import Edificios, UnidadFuncional, Amenities
from .models import ReservaAmeni, ReclamosSugerencias, Gastos


class EdificiosAdmin (admin.ModelAdmin):
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
class AmenitiesAdmin(admin.ModelAdmin):
        pass
class ReservaAmeniAdmin(admin.ModelAdmin):
        pass
    
admin.site.register(Edificios, EdificiosAdmin)
admin.site.register(UnidadFuncional, UnidadFuncionalAdmin)
admin.site.register(Amenities, AmenitiesAdmin)
admin.site.register(ReservaAmeni, ReservaAmeniAdmin)

