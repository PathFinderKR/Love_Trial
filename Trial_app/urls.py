from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    path('nickname/', views.nickname, name='nickname'),
    path('player/', views.player, name='player'),
    path('room/', views.room, name='room'),
    path('chat/', views.chat, name='chat'),
]

