 # reservas/serializers.py

from rest_framework import serializers
from .models import Reserva  # Importa el modelo de reserva (asegúrate de tenerlo definido en models.py)

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'nombre_cliente', 'email_cliente', 'fecha_entrada', 'fecha_salida', 'habitacion', 'estado']

