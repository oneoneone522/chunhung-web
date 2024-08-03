from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username', 'email','password1','password2')

    user=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'輸入您的使用者名稱',
        'class':'username-field'
    }))
    email=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'輸入您的電子郵件地址',
        'class':'email-field'
    }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'輸入您的密碼',
        'class':'username-field'
    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'再次輸入您的密碼',
        'class':'username-field'
    }))
