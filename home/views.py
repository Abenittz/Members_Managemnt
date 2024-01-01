
from django.shortcuts import render, redirect
from .models import Post, Comment, Member
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView

@login_required
def organizer(request):
    list = Member.objects.all()
    user = User.objects.all()
    user_data = []
    
    for users in user:
        user_info = {'username': users.username, 'email': users.email}
        user_data.append(user_info)
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid(): 
            post = form.save(commit=False)
            post.organizer = request.user
            post.save()
            return redirect('organizer_page')
    else:
        form = PostForm() 
    return render(request, 'home/organizer.html', {'form': form, 'list': list, 'users': user_data})

@login_required
def home(request):
    posts = Post.objects.all()
    comment_form = CommentForm()

    return render(request, 'home/home.html', {'posts': posts, 'comment_form': comment_form})

class PostListView(ListView):
    model = Post
    template_name = 'home/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
    
class PostDetailView(DetailView):
    model = Post
    # context_object_name = 'comment_form'

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

def add_comment(request, post_pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.member = request.user.member 
            comment.save()
    else:
        form = CommentForm()
    return redirect('home_detail')
