from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    # path('', views.home, name='home_page'),
    path('', PostListView.as_view(), name='home_page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='home_detail'),
    path('organizer/', views.organizer, name='organizer_page'),
    path('create_post/', views.create_post, name='create_post'),
    path('add_comment/<int:post_pk>/', views.add_comment, name='add_comment'),
]