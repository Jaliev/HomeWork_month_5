from django.urls import path
from movie_app import views


urlpatterns = [
    path('directors_list/', views.DirectorsListCreateAPIView.as_view()),
    path('directors/', views.Directors_with_Movies_ListAPIView.as_view()),
    path('directors/<int:pk>/', views.DirectorRetrieveUpdateDestroyAPIView.as_view()),
    path('movies/', views.MoviesListCreateAPIView.as_view()),
    path('movies/<int:pk>/', views.MovieRetrieveUpdateDestroyAPIView.as_view()),
    path('reviews/', views.ReviewsListCreateAPIView.as_view()),
    path('reviews/<int:pk>/', views.ReviewRetrieveUpdateDestroyAPIView.as_view()),
    path('movies/reviews/', views.Movies_with_Reviews_ListAPIView.as_view()),
]