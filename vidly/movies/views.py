from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies, Genre
# Create your views here.

def index(request):
    movies = Movies.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

def detail(request, movie_id):
    movie = Movies.objects.get(pk=movie_id)
    return render(request, "movies/detail.html", {'movie':movie})
    
