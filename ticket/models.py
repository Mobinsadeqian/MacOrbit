from django.db import models
from django.conf import settings

class Ticket(models.Model):
    DEPARTMENT_CHOICES = [
        ('appleid', 'پشتیبانی خدمات اپل آیدی'),
        ('apps', 'مشکلات دانلود و نصب نرم‌افزار'),
        ('financial', 'امور مالی و پرداخت'),
        ('general', 'سوالات عمومی'),
    ]

    STATUS_CHOICES = [
        ('open', 'باز / در انتظار پاسخ پشتیبان'),
        ('answered', 'پاسخ داده شده'),
        ('user_replied', 'پاسخ کاربر'),
        ('closed', 'بسته شده'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'کم'),
        ('medium', 'متوسط'),
        ('high', 'فوری'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets', verbose_name="کاربر")
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='تیتر')
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES, default='appleid', verbose_name='بخش مربوطه')
    priroty = models.CharField(max_length=10, choices=PRIORITY_CHOICES, null=False, blank=False, verbose_name='اولویت', default='medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=False, blank=False, verbose_name='وضعیت تیکت', default='open')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین به‌روزرسانی")

    class Meta:
        verbose_name = 'تیکت'
        verbose_name = "تیکت‌ها"
        ordering = ['-updated_at']

    def __str__(self):
        return f"تیکت {self.id} - {self.title} ({self.get_status_display()})"

class TicketMessage(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='messages', verbose_name="تیکت مربوطه")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="فرستنده پیام")
    message = models.TextField(verbose_name="متن پیام")

    attachment = models.FileField(upload_to='ticket_attachment/', blank=True, null=True, verbose_name="فایل ضمیمه")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان ارسال")

    class Meta:
        verbose_name = "پیام تیکت"
        verbose_name = "پیام‌های تیکت"
        ordering = ['-created_at']

    def __str__(self):
        return f"پیام از {self.sender} برای تیکت {self.ticket.id}"    