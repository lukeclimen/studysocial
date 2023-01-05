from django.shortcuts import render

# Create your views here.


rooms = [
    {'id': 1, 'name':  "Let's learn Python"},
    {'id': 2, 'name':  "Design with Me"},
    {'id': 3, 'name':  "Front End Developers"},
]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request, primaryKey):
    currentRoom = None
    for room in rooms:
        if room['id'] == int(primaryKey):
            currentRoom = room
            break

    context = {'room':currentRoom}


    return render(request, 'base/room.html', context)
