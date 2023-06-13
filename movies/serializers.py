from rest_framework import serializers
from .models import RatingMovie
from .models import Movie, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField(required=False)
    rating = serializers.ChoiceField(
        choices=RatingMovie.choices, default=RatingMovie.G, required=False
    )
    synopsis = serializers.CharField(required=False)
    added_by = serializers.CharField(read_only=True, source="user.email")

    def create(self, validated_data: dict):
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True, source="movie.title")
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.CharField(read_only=True, source="user.email")
    buyed_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data: dict):
        return MovieOrder.objects.create(**validated_data)
