from rest_framework.views import APIView, Request, Response, status
from .permissions import MyCustomPermission, permissionDelete
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Movie
from .serializers import MovieSerializer, MovieOrderSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MyCustomPermission]

    def get(self, req: Request) -> Response:
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies.order_by("title"), req)
        serializer = MovieSerializer(instance=result_page, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, req: Request) -> Response:
        serializer = MovieSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=req.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieById(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissionDelete]

    def get(self, req: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, req: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        self.check_object_permissions(req, movie)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieOrderById(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, req: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieOrderSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=req.user, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
