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


if __name__ == '__main__':
    request_domain = 'http://127.0.0.1:5000/movies'
    category = 'COSTUME DESIGN (Color)'
    request = request_domain + '/category/' + category

    title = 'The Sound of Music'

    title_request = request_domain + '/title/' + title

    our_response = requests.get(request)
    our_attributes = json.loads(our_response.text)
    print(our_attributes)
    print(len(our_attributes))

    title_response = requests.get(title_request)
    title_attributes = [json.loads(title_response.text)]
    print(title_attributes)
    print(len(title_attributes))
