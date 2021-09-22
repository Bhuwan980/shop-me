from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ['email', 'first_name','username','is_active']
    readonly_fields = ['password']
    list_display_links = ['email', 'first_name']
    ordering = ['-date_joined']
    list_filter = []
    filter_horizontal = []
    fieldsets = ()

admin.site.register(Account, AccountAdmin)