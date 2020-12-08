from django.urls import path

from . import views

urlpatterns = [
    path('/', views.index, name='movie_search_page'),
]
