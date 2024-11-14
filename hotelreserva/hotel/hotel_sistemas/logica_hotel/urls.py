from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from logica_hotel.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'reservaciones', ReservaViewSet)
router.register(r'habitaciones', HabitacionViewSet)

urlpatterns = [

    path('api/', include(router.urls))
]