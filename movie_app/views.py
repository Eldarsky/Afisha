from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieDetailSerializer, MovieSerializer, ReviewSerializer, ReviewDetailSerializer,\
    DirectorSerializer, DirectorDetailSerializer
from .models import Movie, Review, Director


@api_view(['GET'])
def director_view(request):
    director = Director.objects.all()
    serializer = DirectorSerializer(director, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found!'},
                        status=404)
    serializer = DirectorDetailSerializer(director, many=False)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found!'},
                        status=404)
    serializer = ReviewDetailSerializer(reviews, many=False)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found!'},
                        status=404)
    serializer = MovieDetailSerializer(movie, many=False)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)
