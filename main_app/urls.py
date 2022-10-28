from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('movies/', views.movies_index, name='index'),
    path('actors/', views.actors_index, name='index'),
    path('movies/<int:movie_id>/', views.movies_detail, name='movie_detail'),
    path('actors/<int:actor_id>/', views.actors_detail, name='actor_detail'),
    path('movies/<int:movie_id>/add_release/', views.add_release, name='add_release'),
    path('movies/create/', views.MovieCreate.as_view(), name='movies_create'),
    path('actors/create/', views.ActorCreate.as_view(), name='actors_create'),
    path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movies_update'),
    path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movies_delete'),
    path('actors/<int:pk>/update/', views.ActorUpdate.as_view(), name='actors_update'),
    path('actors/<int:pk>/delete/', views.ActorDelete.as_view(), name='actors_delete'),
    path('movies/<int:movie_id>/assoc_actor/<int:actor_id>/', views.assoc_actor, name='assoc_actor'),
]