from django.urls import path
from .views import MovieView, MovieById

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieById.as_view()),
]
