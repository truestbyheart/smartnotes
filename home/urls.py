from django.urls import path

from . import views

urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
]