from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Index page
    path('', views.index, name='index'),

    # Music-related URLs
    path('music_list/', views.music_list, name='music_list'),

    # Authentication-related URLs
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Dashboard view
    path('dashboard/', views.dashboard, name='dashboard'),
]
