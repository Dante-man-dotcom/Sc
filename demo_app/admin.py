from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # your custom user model

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass