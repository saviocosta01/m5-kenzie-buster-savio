from django.urls import path
from .views import MovieView, MovieById, MovieOrderById

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieById.as_view()),
    path("movies/<int:movie_id>/orders/", MovieOrderById.as_view()),
]
