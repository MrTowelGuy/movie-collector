from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Actor

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def movies_index(request):
  movies = Movie.objects.all()
  return render(request, 'movies/index.html', { 'movies': movies })

def actors_index(request):
  actors = Actor.objects.all()
  return render(request, 'actors/index.html', { 'actors': actors })

def movies_detail(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  return render(request, 'movies/detail.html', { 'movie': movie })

def actors_detail(request, actor_id):
  actor = Actor.objects.get(id=actor_id)
  return render(request, 'actors/detail.html', { 'actor': actor })

# # Add the Cat class & list and view function below the imports
# class Movie:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, title, genre, description):
#     self.title = title
#     self.genre = genre
#     self.description = description

# movies = [
#   Movie('Superbad', 'Comedy', 'foul and raunchy'),
#   Movie('Mortal Kombat', 'Action', 'Violent and cheesey'),
#   Movie('Up', 'pixar comedy', 'cute and quaint')
# ]

# class Actor:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, description, age):
#     self.name = name
#     self.description = description
#     self.age = age

# actors = [
#   Actor('Seth Rogan', 'silly', 35),
#   Actor('Tom Holland', 'Young and aspiring', 25),
#   Actor('Cassie Huellete', 'my roommate', 25)
# ]

