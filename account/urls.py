from django.urls import path
from account import views

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('signup/', views.register_user, name='register_user'),
    path('dashboard/', views.user_dashboard, name='user_dashboard')
]