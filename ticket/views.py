from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket, TicketMessage
from django.contrib.auth.decorators import login_required

def register_new_ticket(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get('title')
        department = request.POST.get('department')
        priroty = request.POST.get('priroty')
        message = request.POST.get('message')
        attachment = request.FILES.get('attachment')
        new_ticket = Ticket.objects.create(title=title, department=department, priroty=priroty, user=user)
        TicketMessage.objects.create(ticket=new_ticket, sender= user, message=message, attachment=attachment)
        return redirect('user_dashboard')
    return render(request, 'ticket/register_new_ticket.html')    

@login_required
def ticket_detail(request, ticket_id):
    # تیکت را پیدا میکند؛ مطمئن می‌شویم تیکت مال همین کاربر لاگین شده است
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    
    if request.method == "POST":
        message_text = request.POST.get('message')
        attachment = request.FILES.get('attachment')
        
        if message_text:
        
            TicketMessage.objects.create(
                ticket=ticket,
                sender=request.user,
                message=message_text,
                attachment=attachment
            )
            # ۲. تغییر وضعیت تیکت به "پاسخ کاربر"
            ticket.status = 'user_replied'
            ticket.save()
            
            return redirect('ticket_detail', ticket_id=ticket.id)
            
    # گرفتن تمام پیام‌های این تیکت به ترتیب زمان ارسال
    messages = ticket.messages.all().order_by('created_at') # اگر ریلیشن‌نامت متفاوت است، از TicketMessage.objects.filter(ticket=ticket) استفاده کن
    
    context = {
        'ticket': ticket,
        'messages': messages,
    }
    return render(request, 'ticket/ticket_detail.html', context)