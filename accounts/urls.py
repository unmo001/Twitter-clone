from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import SignUp

app_name = "accounts"

urlpatterns = [
    path('', views.TopPageView.as_view(), name='toppage'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('accounts/signup/', SignUp.as_view(), name='signup'),
    # path('female/', views.FemaleView.as_view(), name='female'),
    # path('male/', views.MaleView.as_view(), name='male')
]
