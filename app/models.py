from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length= 50, null= False, unique= True, primary_key=True) # the genre name is the primary key
    creation_date = models.DateField(auto_now_add= False, null= False)
    description = models.CharField(max_length= 200, null = True)

# creating a table for the songs
class Song(models.Model):
    song_title = models.CharField(max_length= 50, null= False, unique= True, primary_key=True) # the song name is the primary key
    artis_name = models.CharField(max_length= 50, null= False) # this cannot be unique lol (or else every artist would only have one song!
    genre_type = models.ForeignKey(Genre, on_delete=models.CASCADE) # we will use the pk from genre(the genre name)
    #Cascade means that if the key in genre is deleted then all objects with said key will also be deleted
    creation_date = models.DateField(auto_now_add= False, null= False)

# creating a table for artist!
class Artist(models.Model):
    name = models.CharField(max_length= 50, null= False, unique= True, primary_key=True)
    birth_day = models.DateField(auto_now_add= False, null= False)
    monthly_listeners = models.IntegerField(null= False)
    bio = models.CharField(max_length= 400, null= False)
    started_making_music = models.DateField(auto_now_add= False, null= False)




