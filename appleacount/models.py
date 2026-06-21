from django.db import models
from django.conf import settings
class AppleIdOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='apple_id_order', blank=True, null=True)
    fa_firstname = models.CharField(max_length=50, verbose_name="نام (فارسی)")
    fa_lastname = models.CharField(max_length=100, verbose_name="نام خانوادگی (فارسی)")
    en_firstname = models.CharField(max_length=50, verbose_name="نام (انگلیسی)")
    en_lastname = models.CharField(max_length=100, verbose_name="نام خانوادگی (انگلیسی)")
    email = models.EmailField(unique=True, verbose_name="ایمیل کاربر")
    birth_date = models.DateField(verbose_name='تاریخ تولد')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    STATUS_CHOICES = [
        ('pending', 'در انتظار ساخت'),
        ('processing', 'در حال انجام'),
        ('completed', 'تحویل داده شده'),
        ('failed', 'ناموفق'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='وضعیت سفارش')

    def __str__(self):
        return f"سفارش {self.en_firstname} {self.en_lastname} - {self.email}"

