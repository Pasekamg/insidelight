from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.music_list, name='music_list'),
    # Add more URL patterns as needed
]
