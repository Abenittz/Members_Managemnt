from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistration(UserCreationForm):
    email = forms.EmailField()
    name = forms.EmailField()
    f_name = forms.CharField()

    class Meta:
        model = User
        fields = ['name', 'f_name','username', 'email', 'password1']
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))