from django.shortcuts import render

def music_list(request):
    # Logic to fetch and display the music goes here
    return render(request, 'music/music_list.html', {})
# music/views.py

def index(request):
    return render(request, 'music/index.html')  # Make sure 'music/index.html' template exists
