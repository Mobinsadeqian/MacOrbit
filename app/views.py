from django.shortcuts import render, redirect
from .models import MacApp, Category

def macapps(request):
    apps = MacApp.objects.filter(is_published=True)
    Categories = Category.objects.all()
    context = {
        'apps':apps,
        'categories' : Categories,
        
    }
    return render(request, 'apps/macapps.html', context)