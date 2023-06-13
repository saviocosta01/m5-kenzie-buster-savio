from django.db import models
from users.models import User

# Create your models here.]


class RatingMovie(models.TextChoices):
    G = ("G",)
    PG = ("PG",)
    PG13 = ("PG-13",)
    R = ("R",)
    NC17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, blank=True, null=True, default=None)
    rating = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=RatingMovie.choices,
        default=RatingMovie.G,
    )
    synopsis = models.TextField(blank=True, null=True, default=None)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="users",
    )


class MovieOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
