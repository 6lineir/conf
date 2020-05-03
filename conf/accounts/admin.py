from django.contrib import admin
from .models import profile


# Register your models here.

class adminprofile(admin.ModelAdmin):
    list_display = ('user', 'cavatar', 'weburl')

admin.site.register(profile, adminprofile)