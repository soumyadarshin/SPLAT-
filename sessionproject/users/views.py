from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Start a session for the user
            messages.success(request, 'Login successful.')
            return redirect('home')  # Redirect to a homepage or dashboard
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'users/login.html')

# Logout view
def logout_view(request):
    logout(request)  # End the session
    messages.success(request, 'You have been logged out.')
    return redirect('login')  # Redirect to login page
