from django.contrib import admin
from .models import User

class AdminUser(admin.ModelAdmin):
    list_display = ['username', 'is_dealer']


admin.site.register(User, AdminUser)
