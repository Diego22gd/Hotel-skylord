from django.db import models

class Habitacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    capacidad = models.IntegerField()
    estado = models.CharField(max_length=20, choices=[('disponible', 'Disponible'), ('ocupada', 'Ocupada'), ('mantenimiento', 'En Mantenimiento')])

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    cliente_nombre = models.CharField(max_length=100)
    cliente_email = models.EmailField()
    cliente_telefono = models.CharField(max_length=15)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=[('confirmada', 'Confirmada'), ('pendiente', 'Pendiente'), ('rechazada', 'Rechazada')])

    def __str__(self):
        return f"Reserva de {self.cliente_nombre} - {self.estado}"
