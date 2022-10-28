from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('movies/', views.movies_index, name='index'),
    path('actors/', views.actors_index, name='index'),
    path('movies/<int:movie_id>/', views.movies_detail, name='detail'),
    path('actors/<int:actor_id>/', views.actors_detail, name='detail'),
]