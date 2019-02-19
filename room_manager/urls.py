from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('rooms', views.rooms, name='rooms'),
    path('reservations', views.reservations, name='reservations'),
    path('reserve/<int:room_id>', views.make_reservation, name='make_reservation')
]
