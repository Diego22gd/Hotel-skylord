from rest_framework import serializers
from .models import Reserva,Habitacion
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        
        validated_data['password'] = make_password(validated_data['password'])

        return super().create(validated_data)

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'