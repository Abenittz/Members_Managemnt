from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('organizer/', views.organizer, name='organizer_page'),
    path('create_post/', views.create_post, name='create_post'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
]