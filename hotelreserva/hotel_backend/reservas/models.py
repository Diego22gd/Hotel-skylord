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
