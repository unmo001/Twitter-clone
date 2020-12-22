import form as form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.urls import reverse_lazy

from .models import CustomUser, PostModel


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'email', 'gender')


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'


class PostForm(forms.ModelForm):
    success_url = reverse_lazy('accounts:male')
    template_name = 'accounts:male'

    class Meta:
        model = PostModel
        fields = ('text',)
