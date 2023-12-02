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
        fields = ('id', 'title', 'description', 'duration', 'director')

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=False, read_only=True)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director')

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'movie', 'stars')

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=False, read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'text', 'movie', 'stars')

class Movies_with_ReviewSerializer(serializers.ModelSerializer):
    movie_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Review
        fields = ('movie_name', 'text', 'stars')

    def get_movie_name(self, obj):
        if obj.movie is not None:
            return obj.movie.title
        return None

class Directors_with_MoviesSerializer(serializers.ModelSerializer):
    director_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Movie
        fields = ('director_name', 'title')

    def get_director_name(self, obj):
        if obj.director is not None:
            return obj.director.name
        return None

class DirectorsValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

    def validate_name(self, value):
        if len(value) > 100:
            raise serializers.ValidationError('Длина имени должна быть не более 100 символов')

class MoviesValidateSerilizer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    duration = serializers.CharField(max_length=50)
    director_id = serializers.IntegerField()

    def validate_title(self, value):
        if len(value) > 100:
            raise serializers.ValidationError('Длина заголовка должна быть не более 100 символов')

    def validate_director_id(self, value):
        try:
            Director.objects.get(id=value)
        except Director.DoesNotExist:
            raise serializers.ValidationError(f'Режиссёр с id {value} не найден!')
        return value

    def validate_description(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Длина описания должна быть не более 500 символов')

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1500)
    movie_id = serializers.IntegerField()
    stars = serializers.CharField(max_length=5)

    def validate_movie_id(self, value):
        try:
            Movie.objects.get(id=value)
        except Movie.DoesNotExist:
            raise serializers.ValidationError(f'Фильм с id {value} не найден!')
        return value

    def validate_text(self, value):
        if len(value) > 1500:
            raise serializers.ValidationError('Длина отзыва должна быть не больше 1500 символов')