from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def movies_index(request):
  return render(request, 'movies/index.html', { 'movies': movies })

def actors_index(request):
  return render(request, 'actors/index.html', { 'actors': actors })

# Add the Cat class & list and view function below the imports
class Movie:  # Note that parens are optional if not inheriting from another class
  def __init__(self, title, genre, description):
    self.title = title
    self.genre = genre
    self.description = description

movies = [
  Movie('Superbad', 'Comedy', 'foul and raunchy'),
  Movie('Mortal Kombat', 'Action', 'Violent and cheesey'),
  Movie('Up', 'pixar comedy', 'cute and quaint')
]

class Actor:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, description, age):
    self.name = name
    self.description = description
    self.age = age

actors = [
  Actor('Seth Rogan', 'silly', 35),
  Actor('Tom Holland', 'Young and aspiring', 25),
  Actor('Cassie Huellete', 'my roommate', 25)
]