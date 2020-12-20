from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, resolve_url
from django.template import loader
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views import View, generic
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, ModelFormMixin

from accounts.forms import SignUpForm, LoginForm, Post_Form
from .models import CustomUser
from .forms import Test_Model_Form


# Create your views here.


class TopPageView(TemplateView):
    template_name = 'toppage/TopPage.html'


toppageview = TopPageView.as_view()


class IndexView(TemplateView):
    template_name = 'index.html'


indexview = IndexView.as_view()


class FemaleView(TemplateView):
    template_name = 'female.html'
    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super(FemaleView, self).get_context_data()
        context['user'] = self.request.user

        return context


class MaleView(ListView, ModelFormMixin):
    template_name = 'male.html'
    model = CustomUser
    paginate_by = 5
    success_url = reverse_lazy("accounts:male")
    form_class = Post_Form
    
    def __init__(self, **kwargs):
        super().__init__()
        self.object = None
        self.object_list = self.get_queryset()

    def get(self, request, *args, **kwargs):
        self.object = None
        return super(MaleView, self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(MaleView, self).get_context_data()
        context['user'] = self.request.user
        return context

    def post(self, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


maleview = MaleView.as_view()


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'

    def get_success_url(self):
        if self.object.gender == '男':
            target = 'accounts:male'
        else:
            target = 'accounts:female'
        print('target {}'.format(target))
        login(self.request, self.object)
        return reverse(target)


signup = SignUp.as_view()


class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def get_success_url(self):
        if self.request.user.gender == "男":
            target = 'accounts:male'
        else:
            target = 'accounts:female'
        return reverse(target)


class Logout(LogoutView):
    template_name = 'toppage/TopPage.html'


class Template_View(TemplateView):
    template_name = 'generic/templateview.html'

    def get_context_data(self, **kwargs):
        context = super(Template_View, self).get_context_data(**kwargs)
        context['変数キー'] = '表示されるやつ'
        form = Test_Model_Form(self.request)
        return context


templateview = Template_View.as_view()
