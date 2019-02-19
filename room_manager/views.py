from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseServerError
from django.contrib.auth.models import User
from . import models

# Create your views here.


def index(request):
    context = {}
    return render(request, 'room_manager/index.html', context)


def rooms(request):
    rooms = models.Room.objects.all
    context = { 'rooms': rooms }
    return render(request, 'room_manager/rooms.html', context)

def reservations(request):
    reservations = models.Reservation.objects.all
    context = { 'reservations': reservations }
    return render(request, 'room_manager/reservations.html', context)


def make_reservation(request, room_id):
    if request.method == 'GET':
        return render_reservation_form(request, room_id)
    elif request.method == 'POST':
        create_reservation(request)
        return redirect('room_manager.reservations')

def create_reservation(request):
    reservation = models.Reservation()
    reservation.room_id = request.POST['room']
    reservation.organisor_id = request.POST['organisor']
    reservation.startdate = request.POST['startdate']
    reservation.enddate = request.POST['enddate']
    reservation.save()

def render_reservation_form(request, room_id):
    # Get room based on ID
    room = models.Room.objects.get(pk=room_id)
    # Get user or anonymous
    if request.user.is_authenticated:
        organisor = request.user
    elif User.objects.filter(username='Anonymous').exists():
        organisor = User.objects.get(username='Anonymous')
    else:
        return HttpResponseServerError('User `Anonymous` not found in database.')
    context = {
        'room': room,
        'organisor': organisor
    }
    return render(request, 'room_manager/make_reservation.html', context)
