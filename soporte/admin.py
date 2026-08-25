from django.contrib import admin
from .models import Cliente, Tecnico, Reparacion

admin.site.register(Cliente)
admin.site.register(Tecnico)
admin.site.register(Reparacion)
