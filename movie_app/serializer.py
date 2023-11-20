from rest_framework import serializers
from movie_app.models import Director, Movie, Review

class DirectorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name')

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class MoviesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title')

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=False)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director')

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text')

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=False)
    class Meta:
        model = Review
        fields = ('id', 'text', 'movie', 'stars')

class Movies_with_ReviewSerializer(serializers.ModelSerializer):
    movie_name = serializers.SerializerMethodField(read_only=True)
    # rating = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Review
        fields = ('movie_name', 'text', 'stars')

    def get_movie_name(self, obj):
        if obj.movie is not None:
            return obj.movie.title
        return None

    # def get_rating(self, obj):
    #     rating = []
    #     average_score = sum(movie_app.models.Review.stars) / len(movie_app.models.Review.stars)
    #     for i in average_score:
    #         rating.append(i)
    #         return rating


class Directors_with_MoviesSerializer(serializers.ModelSerializer):
    director_name = serializers.SerializerMethodField(read_only=True)
    # movies_count = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Movie
        fields = ('director_name', 'title')

    def get_director_name(self, obj):
        if obj.director is not None:
            return obj.director.name
        return None

    # def get_movies_count(self, obj):
    #     return obj.title.count()