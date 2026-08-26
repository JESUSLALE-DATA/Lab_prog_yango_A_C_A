from django.urls import path
from . import views

urlpatterns = [
    path('tecnicos/', views.lista_tecnicos, name='lista_tecnicos'),

    path(
        'reparaciones/',
        views.lista_reparaciones,
        name='lista_reparaciones'
    ),

    path(
        'reparaciones/eliminar/<int:id>/',
        views.eliminar_reparacion,
        name='eliminar_reparacion'
    ),

    path(
        'reparaciones/editar/<int:id>/',
        views.editar_reparacion,
        name='editar_reparacion'
    ),
]
