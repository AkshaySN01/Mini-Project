from django import forms
from .models import Posts, Users, Comment
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class Post(forms.ModelForm):
    class Meta:
        model=Posts
        fields=['photo','caption']
        widgets={
            'caption':forms.TextInput(attrs={'class':'formstyle'}),
        }

class Edit_user(UserChangeForm):
    class Meta:
        model=Users
        fields=['username','name','photo']


class UserCreation(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirm'}))
    class Meta:
        model=Users
        fields=['Email_Ph_no','name','username',]
        widgets={
            'Email_Ph_no':forms.TextInput(attrs={'class':'form-control','placeholder':'E-Mail'}),
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),    
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels={
            'text':''
        }
        widgets={
            'text':forms.TextInput(attrs={'class':'cmnt','placeholder':'Add a comment'}),
        }