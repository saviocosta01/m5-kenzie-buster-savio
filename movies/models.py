from django.db import models

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
