import requests
import json
from ApiUrl import *


def search_title(api_key, query):
    url = ApiUrl(api_key, query)
    response = requests.get(url.address)  # THIS ACTION CONSUMES AN API HIT, WE GET 1000 PER DAY
    attributes = json.loads(response.text)

    if attributes["Response"] == "True":
        movie_entry = (attributes["Released"], attributes["Plot"], attributes["Poster"])
        return movie_entry
    else:
        print(query + ' was an Invalid Movie')
