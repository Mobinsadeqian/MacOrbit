from django.contrib import admin
from .models import MacApp, Category, DownloadLink

admin.site.register(MacApp)
admin.site.register(Category)
admin.site.register(DownloadLink)