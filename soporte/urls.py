from django.urls import path
from . import views

urlpatterns = [
    path('tecnicos/', views.lista_tecnicos, name='lista_tecnicos'),
    path('tecnicos/crear/', views.crear_tecnico, name='crear_tecnico'),
    path('tecnicos/eliminar/<int:id>/', views.eliminar_tecnico, name='eliminar_tecnico'),

    path('reparaciones/', views.lista_reparaciones, name='lista_reparaciones'),
    path('reparaciones/crear/', views.crear_reparacion, name='crear_reparacion'),
    path('reparaciones/editar/<int:id>/', views.editar_reparacion, name='editar_reparacion'),
    path('reparaciones/eliminar/<int:id>/', views.eliminar_reparacion, name='eliminar_reparacion'),
]
