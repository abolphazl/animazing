from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login_page'),
    path('logout', views.LogoutView.as_view(), name='logout_page'),
    path('register', views.RegisterView.as_view(), name='register_page'),
]