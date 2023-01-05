from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chatroom/<str:primaryKey>/', views.room, name='room'),
]