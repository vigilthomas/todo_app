from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from todo.models import Todos


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control "}),
            'email': forms.EmailInput(attrs={"class": "form-control "}),
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ["name"]
