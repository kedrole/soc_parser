from django.contrib import admin

# Register your models here.

from .models import Href, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'mail_notifications']

admin.site.register(Href)