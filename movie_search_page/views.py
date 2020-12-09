from django.shortcuts import render

from .models import Movie

import requests

import json


# Create your views here.
def index(request, categoryname='all', moviename='all'):
    request_url = 'http://127.0.0.1:5000/movies'

    if categoryname == "COSTUME-DESIGN-Color":
        categoryname = "COSTUME DESIGN (Color)"
    elif categoryname == "COSTUME-DESIGN-Black-and-White":
        categoryname = "COSTUME DESIGN (Black-and-White)"
    elif categoryname == "MAKEUP-AND-HAIRSTYLING":
        categoryname = "MAKEUP AND HAIRSTYLING"

    if moviename != 'all':
        request_url += '/title/' + moviename
    elif categoryname != 'all':
        request_url += '/category/' + categoryname

    response = requests.get(request_url)
    if moviename != 'all':
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

    movie1 = Movie()
    movie1.name = 'Fast and Furious'
    movie1.image = 'https://upload.wikimedia.org/wikipedia/en/8/8f/Fast_and_Furious_Poster.jpg'
    movie1.release_date = '10-22-15'
    movie1.movie_awards = 'Best Actor'
    movie2 = Movie()
    movie2.name = 'GodFather'
    movie2.image = 'https://m.media-amazon.com/images/M' \
                   '/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM' \
                   '@._V1_UY1200_CR107,0,630,1200_AL_.jpg '
    movie2.release_date = '03-04-94'
    movie2.movie_awards = "Best Action Thriller"
    movie3 = Movie()
    movie3.name = 'Larry The Bird'
    movie3.image = 'https://static01.nyt.com/images/2014/08/10/magazine/10wmt/10wmt-superJumbo-v4.jpg'
    movie3.release_date = '03-14-98'
    movie3.movie_awards = 'Best Romantic Comedy'
    #  movies = [movie1, movie2, movie3]
    return render(request, 'MovieList.html', {'movies': movies})
#    return render(request, 'MovieList.html', {'movie1': movie1}, {'movie2': movie2}, {'movie3': movie3})
