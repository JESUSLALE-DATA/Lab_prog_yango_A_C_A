from django.contrib import admin
from django.urls import path, include
from soporte import views  # si tu index está ahí

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # el que ya tenías
    path('soporte/', include('soporte.urls')),  # <- AGREGA ESTA LÍNEA
]