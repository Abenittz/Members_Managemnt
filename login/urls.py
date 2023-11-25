from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login_page'),
    path('signin/', views.signin, name='signin_page')
    
]