from django.shortcuts import render
from django.http import HttpResponseRedirect # redirects me to the passed url
from .models import Genre, Artist
# !!!!!! request must always be the first argument !!!!!!!
from app.models import Genre, Song # importing the two tables we need


# Create your views here.
def index(request): # logic when the person goes on the url
    return render(request, 'index.html')

def new_genre(request):
    if request.method == 'GET':
        return render(request, 'new_genre.html')
    elif request.method == 'POST':
        genre_name = request.POST.get('name') # this will retune what the client put in as name
        genre_date = request.POST.get('creation_date')
        genre_description = request.POST.get('description')
        # this creates an instance for the SQL table with the inputs from client
        Genre.objects.create(
            name=genre_name,
            creation_date=genre_date,
            description=genre_description
        )
        return HttpResponseRedirect('/genres/')



def genres(request):
    genres = Genre.objects.all() # gets all the objects (in a list) ! .all() will be a list!
    return render(request, 'genres.html', {'genres_list': genres})

def genre(request, pk): # genre_id is the pk id!
    genre = Genre.objects.get(name=pk)
    all_genre_music = Song.objects.filter(genre_type = genre) # the filter function returns a QuerySet (like a list) that filters only the elements that have the correct genre type.
    return render(request, 'genre.html', {'genre':genre, 'music_of_the_genre':all_genre_music})

# this is for the tacking page!
def add_track(request):
    if request.method == 'GET': # this is when we first click on the web link
        all_genres = Genre.objects.all() # gets all the objects (in a list) ! .all() will be a list!
        all_artist =Artist.objects.all() # is a list of all artists!
        return render(request, 'add_track.html', {'list_of_genres': all_genres , 'list_of_artists': all_artist})
    elif request.method == 'POST':
        # this will return the input the client entered
        song_name = request.POST.get('song_name')
        artist_name = request.POST.get('artist')
        # this gets the name of the genre object we want
        genre_name = request.POST.get('genre_type')
        #creation date
        creation_date = request.POST.get('creation')
        # this finds the particular genre in question in the genre table! (not just the name)
        the_genre = Genre.objects.get(name=genre_name)
        # have to create an instance of the song and put in on the database
        Song.objects.create(
            song_title=song_name,
            artis_name=artist_name,
            genre_type=the_genre,
            creation_date=creation_date
        )
        return HttpResponseRedirect('/genres/')

# This will be the function that adds an artist to the artist table!
def add_artist(request):
    # when we click on the artist page
    if request.method == 'GET':
        return render(request, 'add_artist.html')
    elif request.method == 'POST':
        artist_name = request.POST.get('name') # the name of the instance in html
        artist_date_of_birth = request.POST.get('birth_day')
        monthly_listers =  request.POST.get('monthly_listeners')
        biography = request.POST.get('bio')
        start_of_career = request.POST.get('started_making_music')
        # now creating the artist!
        Artist.objects.create(
            name=artist_name,
            birth_day=artist_date_of_birth,
            monthly_listeners=monthly_listers,
            bio=biography,
            started_making_music=start_of_career
        )
        return HttpResponseRedirect('/') # have to put the slash so you get redirected to the main page!

def song_page(request, pk): # since in our url's page we have a <str:pk> we need to call pk in our function definition!
        the_song = Song.objects.get(song_title = pk)
        the_genre = the_song.genre_type # passes the object which related to the genre from the tabel (it's a forgen key)
        return render(request, 'song.html', {'song': the_song, 'the_genre':the_genre})





