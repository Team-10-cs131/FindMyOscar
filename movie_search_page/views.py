import json
import re

import requests
from django.shortcuts import render

from .models import Movie


# Create your views here.

def index(request, categoryname='all', moviename='all'):
    request_url = 'http://127.0.0.1:5000/movies'
    # raise NameError(request)

    if "COSTUME-DESIGN-COLOR" in categoryname:
        categoryname = "COSTUME DESIGN (Color)"
    elif "COSTUME-DESIGN-BLACK-AND-WHITE" in categoryname:
        categoryname = "COSTUME DESIGN (Black-and-White)"
    elif "MAKEUP-AND-HAIRSTYLING" in categoryname:
        categoryname = "MAKEUP AND HAIRSTYLING"

    # raise ValueError(categoryname)

    if moviename != 'FindMyOscar_Everything' and moviename != 'all':
        request_url += '/title/' + moviename
    elif categoryname != 'FindMyOscar_Everything' and categoryname != 'all':
        request_url += '/category/' + categoryname

        s = request.build_absolute_uri()
        pattern1 = "z(.*?)z"
        pattern2 = "y(.*?)y"
        year = re.search(pattern1, s).group(1)
        winner = re.search(pattern2, s).group(1)

        # raise ValueError(pattern1)
        # raise ValueError(pattern2)

        if year != '' or winner != '':
            request_url += '?year=' + year
            if winner == 'winner':
                request_url += '&winner=True'

        # raise ValueError(request_url)

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
