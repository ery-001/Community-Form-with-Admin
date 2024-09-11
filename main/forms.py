from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.', required=True)
   
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': '',
            'password1': 'Your password must contain at least 8 characters, including a mix of letters, numbers, and special characters.',
            'password2': 'Enter the same password as above.',
        }

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title", "description", "image")
    