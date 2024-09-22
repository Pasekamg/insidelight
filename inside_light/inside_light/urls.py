# inside_light/urls.py

from django.contrib import admin
from django.urls import path, include
from music import views as music_views  # Importing views from the music app

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route
    path('', music_views.home, name='home'),  # Root URL for home view
    path('music/', include('music.urls')),  # Include music app URLs
]
