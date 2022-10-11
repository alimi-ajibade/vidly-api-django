from dataclasses import fields
from random import choices
from rest_framework import serializers
from django.conf import settings
from .models import Customer, Genre, Movie, MoviePoster, SubcriptionType, WatchList


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["_id", "name"]


class MoviePosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviePoster
        fields = ["id", "image"]

    def create(self, validated_data):
        movie_id = self.context["movie_id"]
        return MoviePoster.objects.create(movie_id=movie_id, **validated_data)


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    images = MoviePosterSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = [
            "_id",
            "title",
            "genre",
            "imdbRating",
            "description",
            "releaseDate",
            "images",
            "promoted",
        ]


class AddMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["title", "genre", "imdbRating", "description", "releaseDate"]


class SubscriptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcriptionType
        fields = ["plan", "monthly_price", "video_quality", "resolution", "devices"]


class CustomerSerializer(serializers.ModelSerializer):
    subscription = SubscriptionTypeSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = ["user_id", "subscription"]


class AddCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["user_id", "subscription"]


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = ["id", "movie"]


class AddWatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = ["user_id", "movie"]

    def create(self, validated_data):
        user_id = self.context["user_id"]
        return WatchList.objects.create(user_id=user_id, **validated_data)
