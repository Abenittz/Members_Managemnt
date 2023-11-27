
from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

def organizer(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.organizer = request.user
            post.save()
            return redirect('organizer_page')
    else:
        form = PostForm()
    return render(request, 'home/organizer.html', {'form': form})

def home(request):
    posts = Post.objects.all()
    comment_form = CommentForm()

    return render(request, 'home/home.html', {'posts': posts, 'comment_form': comment_form})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.organizer = request.user
            post.save()
            return redirect('organizer_page')  # Redirect to the organizer page after successfully creating a post
    else:
        form = PostForm()
    
    return render(request, 'home/home.html', {'form': form})

def add_comment(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.member = request.user.member 
            comment.save()
    return redirect('home_page')
