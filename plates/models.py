#models.py
from django.db import models

class LicensePlate(models.Model):
    plate_number = models.CharField(max_length=10)  # شماره پلاک
    image = models.ImageField(upload_to='plates/')  # تصویر پلاک
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد

    def __str__(self):
        return self.plate_number
