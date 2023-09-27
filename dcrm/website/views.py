from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Checking if logging in
    if request.method == 'POST':

        # Getting username and password from form
        username = request.POST['username']
        password = request.POST['password']

        # Authenticating user
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in!'))
            return redirect('home')
        else:
            messages.error(request, ('Error logging in - please try again...'))
            return redirect('home')
    else:
        
        return render(request, 'home.html', {})

def logout_user(request):
    pass
