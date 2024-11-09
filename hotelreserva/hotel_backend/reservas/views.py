# archivo: views.py
from rest_framework import viewsets
from .models import Reserva
from .serializers import ReservaSerializer
from .models import Habitacion
from .serializers import HabitacionSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer






