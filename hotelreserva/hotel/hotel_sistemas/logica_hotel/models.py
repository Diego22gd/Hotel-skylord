from django.db import models
from django.contrib.auth.models import User

class Habitacion(models.Model):

    status = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50, blank=True,) 
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True)  # Precio
    capacidad = models.IntegerField(blank=True)  # Capacidad de personas
    descripcion = models.TextField(blank=True, null=True)  # Descripción adicional
    creada_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "habitaciones"

    def __str__(self):
        return f"Habitación {self.id}"

class Reserva(models.Model):
    
    #Relacion con la tabla usuarios y habitaciones
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)

    #Verificar si este relacion es correcta
    habitacion_fk = models.ForeignKey(Habitacion, on_delete=models.CASCADE)

    check_in_date = models.DateField()
    check_out_date = models.DateField()
    additional_notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "reservas"

    def __str__(self):

        client_name = self.user_fk.first_name  + " " + self.user_fk.last_name
        return f'Reserva de {client_name} para la habitación nro {self.habitacion_fk}'