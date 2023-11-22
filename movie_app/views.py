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

@api_view(['GET', 'POST'])
def get_directors(request):
    if request.method == 'GET':
        director = Director.objects.all()
        serializer = DirectorsListSerializer(director, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        name = request.data['name']
        director = Director.objects.create(name=name)
        return Response(
            {"message": "Created!",
             "data": DirectorsListSerializer(instance=director, many=False).data
             },
            status=201
        )

@api_view(['GET', 'PUT', 'DELETE'])
def get_directors_by_id(request, directors_id):
    try:
        director = Director.objects.get(id=directors_id)
    except Director.DoesNotExist:
        return Response({f'Режиссёр с id {directors_id} не существует'}, status=404)

    if request.method == 'GET':
        serializer = DirectorSerializer(director)
        return Response(serializer.data)
    elif request.method == 'PUT':
        director.name = request.data['name']
        director.save()
        return Response(
            {"message": "Updated!",
             "data": DirectorSerializer(instance=director, many=False).data
             },
            status=200
        )
    elif request.method == 'DELETE':
        director.delete()
        return Response(
            {"message": "Deleted!"},
            status=204
        )

@api_view(['GET', 'POST'])
def get_movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MoviesListSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        title = request.data['title']
        description = request.data['description']
        duration = request.data['duration']
        director_id = request.data['director_id']
        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director_id=director_id
        )
        return Response(
            {"message": "Created!",
             "data": MoviesListSerializer(instance=movie, many=False).data
             },
            status=201
        )

@api_view(['GET', 'PUT', 'DELETE'])
def get_movies_by_id(request, movies_id):
    try:
        movie = Movie.objects.get(id=movies_id)
    except Movie.DoesNotExist:
        return Response({f'Фильм с id {movies_id} не существует'}, status=404)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'PUT':
# Когда делаю ['title', movie.title] выводит KEY ERROR, без него он работает, поэтому не стал его добавлять...
        movie.title = request.data['title']
        movie.description = request.data['description']
        movie.duration = request.data['duration']
        movie.director_id = request.data['director_id']
        movie.save()
        return Response(
            {"message": "Updated!",
             "data": MovieSerializer(instance=movie, many=False).data
             },
            status=200
        )
    elif request.method == 'DELETE':
        movie.delete()
        return Response(
            {"message": "Deleted!"},
            status=204
        )

@api_view(['GET', 'POST'])
def get_reviews(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        text = request.data['text'],
        movie_id = request.data['movie_id']
        review = Review.objects.create(
            text=text,
            movie_id=movie_id
        )
        return Response(
            {"message": "Created!",
             "data": ReviewListSerializer(instance=review, many=False).data
             },
            status=201
        )
@api_view(['GET', 'PUT', 'DELETE'])
def get_reviews_by_id(request, reviews_id):
    try:
        review = Review.objects.get(id=reviews_id)
    except Review.DoesNotExist:
        return Response({f'Отзыв с id {reviews_id} не существует'}, status=404)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        review.text = request.data['text'],
        review.movie_id = request.data['movie_id']
        review.save()
        return Response(
            {"message": "Updated!",
             "data": ReviewSerializer(instance=review, many=False).data
             },
            status=200
        )
    elif request.method == 'DELETE':
        review.delete()
        return Response(
            {"message": "Deleted!"},
            status=204
        )

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