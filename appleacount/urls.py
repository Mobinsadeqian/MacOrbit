from django.urls import path
from appleacount import views

urlpatterns = [
    path('',views.appleacount_form, name='appleacount_form'),
]