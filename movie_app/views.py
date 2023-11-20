from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Director, Movie, Review
from movie_app.serializer import (
    DirectorsListSerializer,
    DirectorSerializer,
    MoviesListSerializer,
    MovieSerializer,
    ReviewListSerializer,
    ReviewSerializer,
    Movies_with_ReviewSerializer,
    Directors_with_MoviesSerializer
)

@api_view(['GET'])
def get_directors(request):
    director = Director.objects.all()
    serializer = DirectorsListSerializer(director, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_directors_by_id(request, directors_id):
    try:
        director = Director.objects.get(id=directors_id)
    except Director.DoesNotExist:
        return Response({f'Режиссёр с id {directors_id} не существует'}, status=404)

    serializer = DirectorSerializer(director)
    return Response(serializer.data)

@api_view(['GET'])
def get_movies(request):
    movies = Movie.objects.all()
    serializer = MoviesListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_movies_by_id(request, movies_id):
    try:
        director = Movie.objects.get(id=movies_id)
    except Movie.DoesNotExist:
        return Response({f'Фильм с id {movies_id} не существует'}, status=404)

    serializer = MovieSerializer(director)
    return Response(serializer.data)

@api_view(['GET'])
def get_reviews(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_reviews_by_id(request, reviews_id):
    try:
        director = Review.objects.get(id=reviews_id)
    except Review.DoesNotExist:
        return Response({f'Отзыв с id {reviews_id} не существует'}, status=404)

    serializer = ReviewSerializer(director)
    return Response(serializer.data)

@api_view(['GET'])
def get_movies_with_reviews(request):
    reviews = Review.objects.all()
    serializer = Movies_with_ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_directors_with_movies(request):
    movie = Movie.objects.all()
    serializer = Directors_with_MoviesSerializer(movie, many=True)
    return Response(serializer.data)