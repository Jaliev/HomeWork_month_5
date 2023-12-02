from django.contrib import admin
from django.urls import path, include
from afisha.drf_yasg import urlpatterns as yasg_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('movie_app.urls')),
    path('api/v1/', include('users.urls')),
] + yasg_patterns
