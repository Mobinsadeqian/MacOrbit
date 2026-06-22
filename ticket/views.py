from django.shortcuts import render

def register_new_ticket(request):
    return render(request, 'ticket/register_new_ticket.html')
