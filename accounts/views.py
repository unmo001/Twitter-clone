from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView

from accounts.forms import SignUpForm, LoginForm
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


class MaleView(ListView):
    template_name = 'male.html'
    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super(MaleView, self).get_context_data()
        context['user'] = self.request.user
        
        return context


maleview = MaleView.as_view()


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
        login(self.request, user)
        self.object = CustomUser
        return super(SignUp, self).form_valid(form)


class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        form = LoginForm
        if form.is_valid(self.request):
            return redirect('accounts:index')
        else:
            return redirect('accounts:toppage')


class Logout(LogoutView):
    template_name = 'toppage/TopPage.html'
