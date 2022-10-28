from pydoc import describe
from django.db import models
from django.urls import reverse

# Create your models here.

RATINGS = (
    ('G', 'All Ages'),
    ('PG', 'Parental Guidance'),
    ('PG-13', '13 or older'),
    ('R', 'Restricted'),
    ('UR', 'Unrated'),
)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'movie_id': self.id})

class Release(models.Model):
    date = models.DateField('release date')
    rating = models.CharField(
        max_length=5,
        choices=RATINGS,
        default=RATINGS[0][0]
        )
    
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_rating_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']

class Actor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'actor_id': self.id})