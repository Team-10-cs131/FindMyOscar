import json

import requests
from django.shortcuts import render

from .models import Movie


# Create your views here.

def index(request, categoryname, moviename):
    request_url = 'http://127.0.0.1:5000/movies'

    if moviename is not 'all':
        request_url += '/title/' + moviename
    elif categoryname is not 'all':
        request_url += '/category/' + categoryname

    response = requests.get(request_url)
    if moviename is not 'all':
        attributes = [json.loads(response.text)]
    else:
        attributes = json.loads(response.text)

    movies = []

    for movie in attributes:
        movie_entry = Movie()
        movie_entry.name = movie['entity']
        movie_entry.image = movie['poster']
        movie_entry.movie_awards = movie['category']
        movie_entry.release_date = movie['released']
        movies.append(movie_entry)

    return render(request, 'MovieList.html', {'movies': movies})
