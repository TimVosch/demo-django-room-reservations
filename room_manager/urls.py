from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='room_manager.index'),
    path('rooms/', views.rooms, name='room_manager.rooms'),
    path('reservations/', views.reservations, name='room_manager.reservations'),
    path('reserve/<int:room_id>/', views.make_reservation, name='room_manager.make_reservation'),
    path('reservations/<int:reservation_id>/remove', views.delete_reservation,
         name='room_manager.delete_reservation')
]
