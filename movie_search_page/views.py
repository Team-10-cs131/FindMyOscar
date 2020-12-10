import json

import requests
from django.shortcuts import render

from .models import Movie


# Create your views here.

def index(request, categoryname='all', moviename='all'):
    request_url = 'http://127.0.0.1:5000/movies'

    if categoryname == "COSTUME-DESIGN-COLOR":
        categoryname = "COSTUME DESIGN (Color)"
    elif categoryname == "COSTUME-DESIGN-BLACK-AND-WHITE":
        categoryname = "COSTUME DESIGN (Black-and-White)"
    elif categoryname == "MAKEUP-AND-HAIRSTYLING":
        categoryname = "MAKEUP AND HAIRSTYLING"

    if moviename != 'FindMyOscar_Everything' and moviename != 'all':
        request_url += '/title/' + moviename
    elif categoryname != 'FindMyOscar_Everything' and moviename != 'all':
        request_url += '/category/' + categoryname

        portion_count = 1
        year = ''
        winner = ''

        for letter in request:
            if letter == 'z':
                portion_count += 1
            elif portion_count == 2:
                if letter != 'z':
                    year += letter
                else:
                    portion_count += 1
            elif portion_count == 3:
                if letter != '/':
                    winner += letter
                else:
                    portion_count += 1
            else:
                pass

            if year != '' or winner != '':
                request_url += '?year=' + year
                if winner == 'winner':
                    request_url += '&winner=True'

    response = requests.get(request_url)
    if moviename != 'FindMyOscar_Everything' and moviename != 'all':
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
