from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True, default="")
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Tecnico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True, default="")
    especialidad = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Reparacion(models.Model):
    ESTADOS = [
        ('ESPERA', 'En espera'),
        ('REPARANDO', 'En reparación'),
        ('FINALIZADO', 'Finalizado'),
        ('ENTREGADO', 'Entregado'),
    ]

    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    diagnostico = models.TextField(blank=True, default="")
    fecha_entrega = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='ESPERA')
    solucion = models.TextField(blank=True, default="")

    def __str__(self):
        return f"Reparación - {self.tecnico}"
