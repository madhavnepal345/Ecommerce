from django import forms

class Login(forms.Form):
    usernamr=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)