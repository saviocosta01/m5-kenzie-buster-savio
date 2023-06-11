from rest_framework import serializers
from .models import RatingMovie
from users.serializers import UserSerializer
from .models import Movie
from users.models import User


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField(required=False)
    rating = serializers.ChoiceField(
        choices=RatingMovie.choices, default=RatingMovie.G, required=False
    )
    synopsis = serializers.CharField(required=False)
    added_by = serializers.CharField(read_only=True)
    user = UserSerializer()

    def create(self, request, validated_data: dict):
        print("teste")
        # user = User.objects.get(username="lucira_buster2")
        # print(user)
        return Movie.objects.create(**validated_data)
