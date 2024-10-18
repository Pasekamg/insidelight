from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def music_list(request):
    """
    View to fetch and display the list of music.
    """
    return render(request, 'music/music_list.html')


def index(request):
    """
    Home page view.
    """
    return render(request, 'music/index.html')  # Ensure 'music/index.html' template exists


def user_login(request):
    """
    View to handle user login functionality.
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to dashboard after login
        return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    
    # GET request: Display the login form
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def dashboard(request):
    """
    View to display the user dashboard, only accessible for logged-in users.
    """
    return render(request, 'dashboard.html')
