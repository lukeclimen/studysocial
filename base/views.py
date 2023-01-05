from django.shortcuts import render
from .models import Room

# Create your views here.


def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request, primaryKey):
    currentRoom = Room.objects.get(id=primaryKey)
    
    context = {'room':currentRoom}


    return render(request, 'base/room.html', context)
