from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chatroom/<str:primaryKey>/', views.room, name='room'),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:primaryKey>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:primaryKey>/', views.deleteRoom, name="delete-room"),
]