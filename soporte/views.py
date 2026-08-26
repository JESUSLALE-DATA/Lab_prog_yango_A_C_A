from django.shortcuts import render, get_object_or_404, redirect
from .models import Tecnico, Reparacion


def index(request):
    return render(request, 'soporte/index.html')


def lista_tecnicos(request):
    tecnicos = Tecnico.objects.all()
    return render(request, 'soporte/tecnicos.html', {'tecnicos': tecnicos})


def lista_reparaciones(request):
    reparaciones = Reparacion.objects.all()
    return render(request, 'soporte/reparaciones.html', {
        'reparaciones': reparaciones
    })


def eliminar_reparacion(request, id):
    reparacion = get_object_or_404(Reparacion, id=id)
    reparacion.delete()
    return redirect('lista_reparaciones')
def editar_reparacion(request, id):
    reparacion = get_object_or_404(Reparacion, id=id)

    if request.method == 'POST':
        reparacion.diagnostico = request.POST.get('diagnostico')
        reparacion.fecha_entrega = request.POST.get('fecha_entrega')
        reparacion.estado = request.POST.get('estado')
        reparacion.solucion = request.POST.get('solucion')

        reparacion.save()

        return redirect('lista_reparaciones')

    return render(request, 'soporte/editar_reparacion.html', {
        'reparacion': reparacion
    })
