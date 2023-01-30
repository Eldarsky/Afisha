from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieDetailSerializer, MovieSerializer, ReviewSerializer, ReviewDetailSerializer,\
    DirectorSerializer, DirectorDetailSerializer, MovieValidateSerializer, DirectorValidateSerializer, \
    ReviewValidateSerializer
from .models import Movie, Review, Director


@api_view(['GET', 'POST'])
def director_view(request):
    if request.method == 'GET':
        director = Director.objects.all()
        serializer = DirectorSerializer(director, many=True)
        return Response(data=serializer.data)
    if request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        name = serializer.validated_data.get('name')

        director = Director.objects.create(name=name)
        director.save()
        return Response(data=DirectorDetailSerializer(director).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found!'},
                        status=404)
    if request.method == 'GET':
        serializer = DirectorDetailSerializer(director, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = request.data.get('name')

        director.name = name
        director.save()
        return Response(data=DirectorDetailSerializer(director).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found!'},
                        status=404)
    if request.method == 'GET':
        serializer = ReviewDetailSerializer(reviews, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')

        reviews.text = text
        reviews.stars = stars
        reviews.movie_id = movie_id
        reviews.save()
        return Response(data=ReviewDetailSerializer(reviews).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def review_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')

        review = Review.objects.create(text=text, stars=stars, movie_id=movie_id)
        review.save()
        return Response(data=ReviewDetailSerializer(review).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found!'},
                        status=404)
    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')

        movie.title = title
        movie.description = description
        movie.duration = duration
        movie.director_id = director_id
        movie.save()
        return Response(data=MovieDetailSerializer(movie).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def movie_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')

        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        movie.save()
        return Response(data=MovieDetailSerializer(movie).data, status=status.HTTP_201_CREATED)