from django.contrib import admin
from django.urls import path, include
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HabitacionViewSet

router = DefaultRouter()
router.register(r'habitaciones', HabitacionViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('reservas.urls')),
    path('api/', include(router.urls)),  # Asegúrate de que el nombre 'reservas' coincide con el de tu app
]


