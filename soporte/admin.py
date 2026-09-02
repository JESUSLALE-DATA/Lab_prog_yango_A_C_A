from django.contrib import admin
from .models import Cliente, Tecnico, Reparacion


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido', 'email')


@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'especialidad', 'email')
    search_fields = ('nombre', 'apellido', 'especialidad')
    list_filter = ('especialidad',)


@admin.register(Reparacion)
class ReparacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'tecnico', 'estado', 'fecha_entrega', 'diagnostico_corto')
    list_filter = ('estado', 'fecha_entrega')
    search_fields = ('diagnostico', 'solucion', 'tecnico__nombre')
    list_editable = ('estado',)

    def diagnostico_corto(self, obj):
        return (obj.diagnostico[:50] + '...') if len(obj.diagnostico) > 50 else obj.diagnostico
    diagnostico_corto.short_description = 'Diagnóstico'
