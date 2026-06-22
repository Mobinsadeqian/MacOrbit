from django.urls import path
from . import views
urlpatterns = [
    path('', views.register_new_ticket, name='register_new_ticket'),
    path('detail/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
]