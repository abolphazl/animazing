from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.db.models import Q

class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('home_page'))
        login_form = LoginForm()
        return render(request, 'login.html', {'login_form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username_or_email = login_form.cleaned_data.get('username')
            user = User.objects.filter(Q(username=username_or_email) | Q(email=username_or_email)).first()
            if user is not None:
                is_password_correct = user.check_password(login_form.cleaned_data.get('password'))
                if is_password_correct:
                    login(request, user)
                    return redirect(reverse('home_page'))
            login_form.add_error('username', "Username/Email or password is wrong!")
        return render(request, 'login.html', {'login_form': login_form})


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('home_page'))
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password')
            
            if User.objects.filter(username=username).exists():
                register_form.add_error('username', 'This username is taken!')
            elif User.objects.filter(email=email).exists():
                register_form.add_error('email', 'This email is taken!')
            else:
                user = User(username=username, email=email)
                user.set_password(password)
                user.save()
                login(request, user)
                return redirect(reverse('home_page'))
        
        return render(request, 'register.html', {'register_form': register_form})


class LogoutView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(reverse('home_page'))
        logout(request)
        return redirect(reverse('home_page'))