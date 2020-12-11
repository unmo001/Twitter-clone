from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from accounts.forms import SignUpForm
from django.http import HttpResponseRedirect, HttpResponse;
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


femaleview = FemaleView.as_view()


class MaleView(TemplateView):
    template_name = 'male.html'


maleview = MaleView.as_view()


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    get_success_url = reverse_lazy('accounts:index')

    def form_valid(self, form):
        form.save()
        gender = form.cleaned_data.get('gender')
        user = authenticate(gender=gender)
        login(self.request, user)
        if gender == '男':
            return HttpResponse('male')
        else:
            return HttpResponse('female')
        # return HttpResponseRedirect(self.get_success_url)


Signup = SignUp.as_view()
