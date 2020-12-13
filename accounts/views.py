from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from accounts.forms import SignUpForm, LoginForm
from django.http import HttpResponseRedirect, HttpResponse, request
from .models import CustomUser


# Create your views here.


class TopPageView(TemplateView):
    template_name = 'toppage/TopPage.html'


toppageview = TopPageView.as_view()


class IndexView(TemplateView):
    template_name = 'index.html'


indexview = IndexView.as_view()


class FemaleView(TemplateView):
    template_name = 'female.html'


def malepage(request):
    gender_show = CustomUser.gender
    template = loader.get_template('male.html')
    return render(request, 'male.html', )


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    
    def get_success_url(self):
        if self.object.gender == '男':
            target = 'accounts:male'
        else:
            target = 'accounts:female'
        return reverse(target)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        self.object = CustomUser
        return super(SignUp, self).form_valid(form)


# class Login(LoginView):
#     form_class = LoginForm
#     template_name = 'login.html'
#
#
# loginview = Login.as_view()
