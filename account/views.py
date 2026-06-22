from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

User = get_user_model()

def login_user(request):
    if request.user.is_authenticated:
        return redirect('user_dashboard')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("user_password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_dashboard')
        else:
            messages.error(request, "نام کاربری یا رمز عبور اشتباه است!")
    return render(request, 'account/login.html')

def register_user(request):
    if request.method == "POST":
        customer_name = request.POST.get('customer_name')
        customer_familyname = request.POST.get('customer_familyname')
        customer_username = request.POST.get('customer_username')
        customer_email = request.POST.get('customer_email')
        customer_password = request.POST.get('customer_password')
        user = User.objects.create_user(name=customer_name,username=customer_username, familyname = customer_familyname, email = customer_email, password = customer_password)
        return redirect('login_user')

    return render(request, 'account/signup.html')

@login_required(login_url='login_user')
def user_dashboard(request):
    return render(request, 'account/user_dashboard.html')

def logout_user(request):
    auth_logout(request)  
    return redirect('login_user')