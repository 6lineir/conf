from django.db import models
from django.contrib.auth.models import User

from django.utils.html import format_html

# Create your models here.

class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True, verbose_name='اواتار')
    weburl = models.URLField(blank=True, verbose_name='ادرس وب')
    
    def cavatar(self):
        return format_html("<img width='50' height='40' style='border-radius:20                                                                                                                                                                                                                                                                                                                                                                                                                                                 px;' src='{}'>".format(self.avatar.url))