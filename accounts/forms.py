from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.forms import Form

from accounts.models import CustomUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'email', 'gender')


class LoginForm(AuthenticationForm):
    class Meta:
        fields = ('username','password1')