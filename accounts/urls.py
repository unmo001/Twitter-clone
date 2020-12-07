from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path('', views.TopPageView.as_view(), name='toppage'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="TopPage.html"), name='logout'),
    path('index/', views.IndexView.as_view(), name='index')
]
