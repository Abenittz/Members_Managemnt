
from django.shortcuts import render, redirect
from .forms import UserRegistration
from django.contrib import messages



def signin(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login_page')
    else:
        form = UserRegistration()
    return render(request, 'login/signin.html', {'form': form})
