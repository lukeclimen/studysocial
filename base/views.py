from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

# Create your views here.


def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request, primaryKey):
    currentRoom = Room.objects.get(id=primaryKey)
    
    context = {'room':currentRoom}
    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        # Save the form data in the database if it's valid
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, primaryKey):
    room = Room.objects.get(id=primaryKey)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        # Replace the existing room instead of making a new instance
        form = RoomForm(request.POST, instance=room)
        # Save the form data in the database if it's valid
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'base/room_form.html', context)