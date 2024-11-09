# archivo: models.py
from django.db import models

class Reserva(models.Model):
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=20)
    room_type = models.CharField(max_length=50)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    additional_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Reserva de {self.client_name} para {self.room_type}'



class Habitacion(models.Model):
    status = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50, blank=True, null=True)  # Tipo de habitación
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Precio
    capacidad = models.IntegerField(blank=True, null=True)  # Capacidad de personas
    descripcion = models.TextField(blank=True, null=True)  # Descripción adicional
    creada_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Habitación {self.id} - {self.status}"
