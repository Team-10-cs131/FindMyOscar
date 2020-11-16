from django.urls import path

from . import views

urlpatterns = [
    path('ragnorak', views.index, name='profile'),
]
