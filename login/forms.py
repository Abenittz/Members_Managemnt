from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistration(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Disable help text for the fields
        for field_name in ['first_name', 'last_name', 'username','email', 'password1', 'password2']:
            self.fields[field_name].help_text = None
            self.fields[field_name].widget.attrs.update({'class': 'form-control', 'style': 'margin-bottom: 20px; background-color: #333; border: none; color: white;'})
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
class LoginForm(forms.Form):
    # username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 20px; background-color: #333; border: none; color: white;' }))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control' , 'style': 'margin-bottom: 20px; background-color: #333; border: none; color: white;'}))
    
    username = forms.CharField(
        max_length=30, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    
  