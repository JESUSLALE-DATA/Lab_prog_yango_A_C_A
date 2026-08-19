from django.urls import path
from . import views

urlpatterns = [
    path('tecnicos/', views.lista_tecnicos, name='lista_tecnicos'),
]