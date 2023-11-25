from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def signin(request):
    if request.method == 'POST':
        # Use request.POST.get('field_name') to get values from form fields
        name = request.POST.get('name')
        f_name = request.POST.get('f_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check for empty fields
        if not name or not f_name or not username or not email or not password:
            messages.error(request, "Please fill in all fields.")
            return redirect('signin_page')  # Use 'return' to make sure the redirect happens
            
        # Check if username or email already exists
        if User.objects.filter(username=username, email=email).exists():
            messages.error(request, "Username or email already exists.")
            return redirect('signin_page')  # Use 'return' to make sure the redirect happens
        else:
        # Create and save the user
            user = User(name=name, f_name=f_name, email=email, username=username, password=password)
            user.save()
        
            messages.success(request, "Registered successfully for {username}.")
            return redirect('login_page')  # Use 'return' to make sure the redirect happens
            
    return render(request, 'login/signin.html')

        
def login(request):
    return render(request, 'login/login.html')