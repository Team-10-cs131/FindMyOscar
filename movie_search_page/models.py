from django.db import models


# Create your models here.

class Movie(models.Model):
    name: str
    image: str
    release_date: str
    movie_awards: str
