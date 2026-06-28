from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name='نام')
    familyname = models.CharField(max_length=50, null=False, blank=False, verbose_name='نام خانوادگی')
    REQUIRED_FIELDS = ['name', 'familyname', 'email']
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.familyname}"
