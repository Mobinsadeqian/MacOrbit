from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import AppleIdOrder
from django.contrib.auth.decorators import login_required

@login_required(login_url='/account/login/')
def appleacount_form(request):
    if request.method == "POST":
        fa_firstname = request.POST.get('fa_firstname')
        fa_lastname = request.POST.get('fa_lastname')
        en_firstname = request.POST.get('en_firstname')
        en_lastname = request.POST.get('en_lastname')
        email = request.POST.get('user_email')
        birth_date = request.POST.get('user_birthdate')

        AppleIdOrder.objects.create(
            user=request.user,
            fa_firstname=fa_firstname,
            fa_lastname=fa_lastname,
            en_firstname=en_firstname,
            en_lastname=en_lastname,
            email=email,
            birth_date=birth_date
        )
        return redirect('home')
        
    return render(request, 'appleacount_form.html')