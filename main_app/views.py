from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie, Actor
from .forms import ReleaseForm
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
  release_form = ReleaseForm()
  return render(request, 'movies/detail.html', {
     'movie': movie, 'release_form': release_form })

def add_release(request, movie_id):
  form = ReleaseForm(request.POST)
  if form.is_valid():
    new_release = form.save(commit=False)
    new_release.movie_id = movie_id
    new_release.save()
  return redirect('movie_detail', movie_id=movie_id)

class MovieCreate(CreateView):
  model = Movie
  fields = ['title','genre','description',]
  success_url = '/movies/'

class MovieUpdate(UpdateView):
  model = Movie
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['title','genre','description',]
  success_url = '/movies/'

class MovieDelete(DeleteView):
  model = Movie
  success_url = '/movies/'

class ActorCreate(CreateView):
  model = Actor
  fields = ['name','description','age']
  success_url = '/actors/'

class ActorUpdate(UpdateView):
  model = Actor
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['name','description','age']
  success_url = '/actors/'


class ActorDelete(DeleteView):
  model = Actor
  success_url = '/actors/'

def actors_detail(request, actor_id):
  actor = Actor.objects.get(id=actor_id)
  return render(request, 'actors/detail.html', { 'actor': actor })

