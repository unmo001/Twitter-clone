from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.forms.forms import Form


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'email','gender')
