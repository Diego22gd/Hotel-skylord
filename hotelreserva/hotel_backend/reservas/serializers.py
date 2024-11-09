 # reservas/serializers.py
# archivo: serializers.py
from rest_framework import serializers
from .models import Reserva
from .models import Habitacion

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'


