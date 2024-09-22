from django.shortcuts import render

def music_list(request):
    # Logic to fetch and display the music goes here
    return render(request, 'music/music_list.html', {})
# music/views.py

def home(request):
    return render(request, 'music/home.html')  # Make sure 'music/home.html' template exists
