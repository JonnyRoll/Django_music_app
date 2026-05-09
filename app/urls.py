# in here is the continuation creates a new path
from django.contrib import admin
from django.urls import path, include
from .views import index, genres, new_genre, genre

urlpatterns = [
    path('', index),
    path('genres/', genres),
    path('genres/create/', new_genre),
    path('genres/<int:pk>/', genre) # dynamic url (ex: genres/1/) where 1 is the number on the list --> pk = primary key
]
