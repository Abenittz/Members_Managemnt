from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Members
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend

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
        if Members.objects.filter(username=username, email=email).exists():
            messages.error(request, "Username or email already exists.")
            return redirect('signin_page')  # Use 'return' to make sure the redirect happens
        else:
        # Create and save the user
            user = Members(name=name, f_name=f_name, email=email, username=username, password=password)
            user.save()
        
            messages.success(request, "Registered successfully for {username}.")
            return redirect('login_page')  # Use 'return' to make sure the redirect happens
            
    return render(request, 'login/signin.html')

class MembersBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user =Members.objects.get(username=username)
        except Members.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        return None

        
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Please enter both username and password.')
            return redirect('login_page')

        # Authenticate against the Members model
        user = authenticate(request, username=username, password=password)

        if user is not None:
           
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('signin_page')  # Redirect to your home page
        else:
            messages.error(request, 'Invalid username or password.')
            
    return render(request, 'login/login.html')
