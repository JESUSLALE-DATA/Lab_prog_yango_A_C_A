from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Tecnico, Reparacion


def index(request):
    context = {
        'total_tecnicos': Tecnico.objects.count(),
        'total_reparaciones': Reparacion.objects.count(),
        'en_espera': Reparacion.objects.filter(estado='ESPERA').count(),
        'en_reparacion': Reparacion.objects.filter(estado='REPARANDO').count(),
        'finalizadas': Reparacion.objects.filter(estado='FINALIZADO').count(),
        'entregadas': Reparacion.objects.filter(estado='ENTREGADO').count(),
    }
    return render(request, 'soporte/index.html', context)


def lista_tecnicos(request):
    tecnicos = Tecnico.objects.all().order_by('nombre')
    return render(request, 'soporte/tecnicos.html', {'tecnicos': tecnicos})


def crear_tecnico(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        apellido = request.POST.get('apellido', '').strip()
        especialidad = request.POST.get('especialidad', '').strip()
        email = request.POST.get('email', '').strip() or None

        if nombre and especialidad:
            Tecnico.objects.create(
                nombre=nombre,
                apellido=apellido,
                especialidad=especialidad,
                email=email
            )
            messages.success(request, f'Técnico {nombre} {apellido} creado correctamente.')
            return redirect('lista_tecnicos')
        messages.error(request, 'Nombre y especialidad son obligatorios.')

    return render(request, 'soporte/crear_tecnico.html')


def eliminar_tecnico(request, id):
    tecnico = get_object_or_404(Tecnico, id=id)
    nombre = f"{tecnico.nombre} {tecnico.apellido}"
    tecnico.delete()
    messages.success(request, f'Técnico {nombre} eliminado.')
    return redirect('lista_tecnicos')


def lista_reparaciones(request):
    reparaciones = Reparacion.objects.select_related('tecnico').all().order_by('-id')
    return render(request, 'soporte/reparaciones.html', {
        'reparaciones': reparaciones
    })


def crear_reparacion(request):
    tecnicos = Tecnico.objects.all().order_by('nombre')

    if request.method == 'POST':
        tecnico_id = request.POST.get('tecnico')
        diagnostico = request.POST.get('diagnostico', '').strip()
        fecha_entrega = request.POST.get('fecha_entrega') or None
        estado = request.POST.get('estado', 'ESPERA')
        solucion = request.POST.get('solucion', '').strip()

        if tecnico_id:
            tecnico = get_object_or_404(Tecnico, id=tecnico_id)
            Reparacion.objects.create(
                tecnico=tecnico,
                diagnostico=diagnostico,
                fecha_entrega=fecha_entrega,
                estado=estado,
                solucion=solucion
            )
            messages.success(request, 'Reparación creada correctamente.')
            return redirect('lista_reparaciones')
        messages.error(request, 'Debes seleccionar un técnico.')

    return render(request, 'soporte/crear_reparacion.html', {
        'tecnicos': tecnicos,
        'estados': Reparacion.ESTADOS
    })


def editar_reparacion(request, id):
    reparacion = get_object_or_404(Reparacion, id=id)

    if request.method == 'POST':
        reparacion.diagnostico = request.POST.get('diagnostico', '')
        reparacion.fecha_entrega = request.POST.get('fecha_entrega') or None
        reparacion.estado = request.POST.get('estado', 'ESPERA')
        reparacion.solucion = request.POST.get('solucion', '')
        reparacion.save()
        messages.success(request, 'Reparación actualizada correctamente.')
        return redirect('lista_reparaciones')

    return render(request, 'soporte/editar_reparacion.html', {
        'reparacion': reparacion
    })


def eliminar_reparacion(request, id):
    reparacion = get_object_or_404(Reparacion, id=id)
    reparacion.delete()
    messages.success(request, 'Reparación eliminada.')
    return redirect('lista_reparaciones')
