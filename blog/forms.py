from django.forms import ModelForm
from django import forms
from .models import BlogModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput,max_length=255)

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title','post','image']
        # widgets = {
        #     'title':forms.TextInput(
        #         attrs={
        #             'class':'form-control',
        #             'placeholder':'Title'
        #         }
        #     ),
        #     'post':forms.Textarea(
        #         attrs={
        #             'class':'form-control',
        #             'placeholder':'Aza',
        #         }
        #     ),
        #     'image':forms.FileInput(
        #         attrs={
        #             'class':'form-control',
        #         }
        #     )
       # }