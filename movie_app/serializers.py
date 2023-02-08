from rest_framework import serializers
from .models import Movie, Review, Director
from rest_framework.exceptions import ValidationError


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name count'.split()


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text movie stars'.split()


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text movie stars'.split()


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    movie_reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'id movie_reviews rating title description duration director'.split()


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.CharField()
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError(f'Director with id ({director_id}) does not exist')
        return director_id


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField()


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField()
    movie_id = serializers.IntegerField()

    def validate_movie_id(self, movie_id):
        try:
            Review.objects.get(id=movie_id)
        except Review.DoesNotExist:
            raise ValidationError(f'Movie with id ({movie_id}) does not exist')
        return movie_id
