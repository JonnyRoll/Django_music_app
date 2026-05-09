from django.shortcuts import render
from django.http import HttpResponseRedirect # redirects me to the passed url
from .models import Genre
# !!!!!! request must always be the first argument !!!!!!!
from app.models import Genre


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
    genre = Genre.objects.get(id=pk)
    return render(request, 'genre.html', {'genre':genre})