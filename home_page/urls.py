from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inception', views.index, name='Movie Name'),
    path('best_animation', views.index, name='Best Animation Category'),
    path('best_male_lead', views.index, name='Male Lead Categpry'),
    path('all', views.index, name='All Category')
]
