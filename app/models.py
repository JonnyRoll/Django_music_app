from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length= 50, null= False, unique= True, primary_key=True) # the genre name is the primary key
    creation_date = models.DateField(auto_now_add= False, null= False)
    description = models.CharField(max_length= 200, null = True)

# creating a table for the songs
class Artist(models.Model):
    song_title = models.CharField(max_length= 50, null= False, unique= True, primary_key=True) # the song name is the primary key
    artis_name = models.CharField(max_length= 50, null= False, unique= True)
    genre_type = models.ForeignKey(Genre, on_delete=models.CASCADE)  # we will use the pk from genre(the genre name)
    #Cascade means that if the key in genre is deleted then all objects with said key will also be deleted


