from django.contrib import admin
from django.urls import path
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/directors/', views.get_directors_with_movies),
    path('api/v1/directors/<int:directors_id>/', views.get_directors_by_id),
    path('api/v1/movies/', views.get_movies),
    path('api/v1/movies/<int:movies_id>/', views.get_movies_by_id),
    path('api/v1/reviews/', views.get_reviews),
    path('api/v1/reviews/<int:reviews_id>/', views.get_reviews_by_id),
    path('api/v1/movies/reviews/', views.get_movies_with_reviews),
]
