# in here is the continuation creates a new path
from django.contrib import admin
from django.urls import path, include
from .views import index, genres, new_genre, genre, add_track, add_artist, song_page, artist_page, delete_song

urlpatterns = [
    path('', index),
    path('genres/', genres),
    path('genres/create/', new_genre),
    path('genres/<str:pk>/', genre), # dynamic url (ex: genres/1/) where 1 is the number on the list --> pk = primary key
    path('add_track/', add_track),
    path('add_artist/', add_artist),
    path('song/<str:pk>/', song_page),
    path('<str:pk>/', artist_page),
    path('song/<str:pk>/delete/', delete_song)
]
