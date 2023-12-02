from django.urls import path
from users import views


urlpatterns = [
    path('login/', views.LoginAPIView.as_view()),
    path('logout/', views.LogoutAPIView.as_view()),
    path('register/', views.RegisterAPIView.as_view()),
    path('verify/', views.VerifyAPIView.as_view()),
    path('profile/', views.ProfileViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('profile/<int:pk>/', views.ProfileViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
    })),
]