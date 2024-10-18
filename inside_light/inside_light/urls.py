from django.contrib import admin
from django.urls import path, include
from music import views as music_views  # Import views from the music app

urlpatterns = [
    # Admin route
    path('admin/', admin.site.urls),

    # Root URL for index view from the music app
    path('', music_views.index, name='index'),

    # Include URLs from the music app
    path('music/', include('music.urls')),

    # Authentication-related URLs (optional, if not already in music.urls)
    path('login/', music_views.user_login, name='login'),
]
