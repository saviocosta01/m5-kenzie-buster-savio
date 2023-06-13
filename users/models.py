from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(blank=True, null=True)
    is_employee = models.BooleanField(blank=True, null=True, default=False)
    movies = models.ManyToManyField(
        "movies.Movie", through="movies.MovieOrder", related_name="users"
    )
