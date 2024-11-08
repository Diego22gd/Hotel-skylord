from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('reservas.urls')),  # Asegúrate de que el nombre 'reservas' coincide con el de tu app
]


