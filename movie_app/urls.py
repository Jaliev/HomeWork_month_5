from django.urls import path
from movie_app import views


urlpatterns = [
    path('directors/', views.get_directors),
    path('directors/<int:directors_id>/', views.get_directors_by_id),
    path('movies/', views.get_movies),
    path('movies/<int:movies_id>/', views.get_movies_by_id),
    path('reviews/', views.get_reviews),
    path('reviews/<int:reviews_id>/', views.get_reviews_by_id),
    path('movies/reviews/', views.get_movies_with_reviews),
]