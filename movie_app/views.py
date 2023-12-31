from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from movie_app.models import Director, Movie, Review
from movie_app.serializer import (
    DirectorsListSerializer, DirectorSerializer, MoviesListSerializer,
    MovieSerializer, ReviewListSerializer, ReviewSerializer,
    Movies_with_ReviewSerializer, Directors_with_MoviesSerializer,
    DirectorsValidateSerializer, MoviesValidateSerilizer, ReviewValidateSerializer
)


'''Метод с использованием CBV - Class Based Views'''

class DirectorsListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorsListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'id']

class DirectorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]

class MoviesListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'title', 'description', 'duration', 'director']

class MovieRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

class ReviewsListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id']

class ReviewRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

class Movies_with_Reviews_ListAPIView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = Movies_with_ReviewSerializer

class Directors_with_Movies_ListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = Directors_with_MoviesSerializer
    permission_classes = [AllowAny]


'''Метод с использованием FBV - Function Based Views'''

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def get_directors(request):
#     if request.method == 'GET':
#         director = Director.objects.all()
#         serializer = DirectorsListSerializer(director, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = DirectorsValidateSerializer(data=request.data)
        # вариант №1
        # if not serializer.is_valid():
        #     return Response(
        #         data={
        #             "message": "Error!",
        #             "data": serializer.errors
        #         },
        #         status=400
        #     )
        # вариант №2
        # serializer.is_valid(raise_exception=True)
        # name = request.data['name']
        # director = Director.objects.create(name=name)
        # return Response(
        #     {"message": "Created!",
        #      "data": DirectorsListSerializer(instance=director, many=False).data
        #      },
        #     status=201
        # )

# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def get_directors_by_id(request, directors_id):
#     try:
#         director = Director.objects.get(id=directors_id)
#     except Director.DoesNotExist:
#         return Response({f'Режиссёр с id {directors_id} не существует'}, status=404)
#
#     if request.method == 'GET':
#         serializer = DirectorSerializer(director)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = DirectorsValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         director.name = request.data['name']
#         director.save()
#         return Response(
#             {"message": "Updated!",
#              "data": DirectorSerializer(instance=director, many=False).data
#              },
#             status=200
#         )
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(
#             {"message": "Deleted!"},
#             status=204
#         )

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def get_movies(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MoviesListSerializer(movies, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = MoviesValidateSerilizer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         title = request.data['title']
#         description = request.data['description']
#         duration = request.data['duration']
#         director_id = request.data['director_id']
#         movie = Movie.objects.create(
#             title=title,
#             description=description,
#             duration=duration,
#             director_id=director_id
#         )
#         return Response(
#             {"message": "Created!",
#              "data": MoviesListSerializer(instance=movie, many=False).data
#              },
#             status=201
#         )

# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def get_movies_by_id(request, movies_id):
#     try:
#         movie = Movie.objects.get(id=movies_id)
#     except Movie.DoesNotExist:
#         return Response({f'Фильм с id {movies_id} не существует'}, status=404)
#
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = MoviesValidateSerilizer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         movie.title = request.data['title']
#         movie.description = request.data['description']
#         movie.duration = request.data['duration']
#         movie.director_id = request.data['director_id']
#         movie.save()
#         return Response(
#             {"message": "Updated!",
#              "data": MovieSerializer(instance=movie, many=False).data
#              },
#             status=200
#         )
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(
#             {"message": "Deleted!"},
#             status=204
#         )

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def get_reviews(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         serializer = ReviewListSerializer(reviews, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ReviewValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         text = request.data['text'],
#         movie_id = request.data['movie_id']
#         review = Review.objects.create(
#             text=text,
#             movie_id=movie_id
#         )
#         return Response(
#             {"message": "Created!",
#              "data": ReviewListSerializer(instance=review, many=False).data
#              },
#             status=201
#         )

# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def get_reviews_by_id(request, reviews_id):
#     try:
#         review = Review.objects.get(id=reviews_id)
#     except Review.DoesNotExist:
#         return Response({f'Отзыв с id {reviews_id} не существует'}, status=404)
#
#     if request.method == 'GET':
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ReviewValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         review.text = request.data['text'],
#         review.movie_id = request.data['movie_id']
#         review.save()
#         return Response(
#             {"message": "Updated!",
#              "data": ReviewSerializer(instance=review, many=False).data
#              },
#             status=200
#         )
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(
#             {"message": "Deleted!"},
#             status=204
#         )

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_movies_with_reviews(request):
#     reviews = Review.objects.all()
#     serializer = Movies_with_ReviewSerializer(reviews, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_directors_with_movies(request):
#     movie = Movie.objects.all()
#     serializer = Directors_with_MoviesSerializer(movie, many=True)
#     return Response(serializer.data)