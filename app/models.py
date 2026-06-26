from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    title_en = models.CharField(max_length=100, unique=True, verbose_name='نام انگلیسی دسته‌بندی')
    title_fa = models.CharField(max_length=100, verbose_name='نام فارسی دسته‌بندی')
    slug = models.SlugField(max_length=120, unique=True, blank=True, verbose_name='اسلاگ (سئو)')

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.title_fa

class MacApp(models.Model):

    class ArchitectureChoices(models.TextChoices):
        INTEL = 'intel', 'Intel Only (مک‌های قدیمی)'
        APPLE_SILiCON = 'm_series', 'Apple Silicon Native (سری M)'
        UNIVERSAL = 'universal', 'Universal (هر دو سری پردازنده)'

    class LicenseChoices(models.TextChoices):
        FREE = 'free', 'کاملاً رایگان'
        CRACKED = 'cracked', 'کرک شده'
        PRE_ACTIVATED = 'pre_activated', 'از قبل فعال شده'

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='apps', verbose_name='دسته‌بندی')
    title_en = models.CharField(max_length=200, verbose_name='نام انگلیسی برنامه')
    title_fa = models.CharField(max_length=200, verbose_name='نام فارسی برنامه')
    slug = models.SlugField(max_length=250, unique=True, blank=True, verbose_name='اسلاگ (سئو)')
    description = models.TextField(verbose_name='توضیحات کامل')
    icon = models.ImageField(upload_to='apps/icons/', verbose_name='آیکون برنامه')

    version = models.CharField(max_length=50, verbose_name='آخرین نسخه')
    developer = models.CharField(max_length=100, blank=True, null=True, verbose_name='توسعه‌دهنده')
    file_size = models.CharField(max_length=50, verbose_name='حجم فایل')
    min_macos = models.CharField(max_length=100, verbose_name='حداقل سیستم‌عامل مورد نیاز')
    architecture = models.CharField(max_length=20, choices=ArchitectureChoices, default=ArchitectureChoices.UNIVERSAL, verbose_name='معماری پردازنده' )

    license_status = models.CharField(
        max_length=20, choices=LicenseChoices.choices, default=LicenseChoices.CRACKED, verbose_name='وضعیت لایسنس'  
    )               
    installation_guide = models.TextField(blank=True, null=True, verbose_name='راهنمای نصب و فعال‌سازی')
    views_count = models.PositiveIntegerField(default=True, verbose_name='تعداد بازدید')
    is_published = models.BooleanField(default=True, verbose_name='وضعیت انتشار')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین به‌روزرسانی')

    class Meta:
        verbose_name = 'نرم‌افزار مک'
        verbose_name_plural = 'نرم‌افزارهای مک'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title_en} (v{self.version})"

class DownloadLink(models.Model):
    app = models.ForeignKey(MacApp, on_delete=models.CASCADE, related_name='download_links', verbose_name='نرم‌افزار مربوطه')
    title = models.CharField(max_length=150, verbose_name='عنوان لینک')
    url = models.URLField(max_length=500, verbose_name='آدرس لینک دانلود')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'لینک دانلود'
        verbose_name_plural = "لینک‌های دانلود"

    def __str__(self):
        return    f"لینک برای {self.app.title_en} - {self.title}"     

