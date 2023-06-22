from django.contrib import admin
from .models import *

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
        # Campos a mostrar en la lista de registros del modelo
        list_display = ['unidad_funcional', 'piso', 'dpto', 'edificio', 'usuario']
        
class AmenityAdmin(admin.ModelAdmin):
        list_display = ['descripcion', 'horarios']

class ReservaAdmin(admin.ModelAdmin):
        list_display = ['fecha', 'horario', 'numero_unidad', 'tipo_amenity']

        def numero_unidad(self, obj):
                return obj.unidad_funcional.unidad_funcional
        
        def tipo_amenity(self, obj):
                return obj.amenity.descripcion
        
class ReclamoAdmin(admin.ModelAdmin):
        list_display = ['fecha', 'asunto', 'descripcion', 'usuario']

admin.site.register(Edificio, EdificioAdmin)
admin.site.register(UnidadFuncional, UnidadFuncionalAdmin)
admin.site.register(Amenity, AmenityAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(ReclamoSugerencia, ReclamoAdmin)

