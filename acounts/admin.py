from django.contrib import admin
from django.contrib.auth.admin  import UserAdmin #Used for AbstractUser Authentication
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username','email','is_student','is_staff_member','is_staff','is_superuser')

    list_filter = ('is_student','is_staff_member','is_staff','is_superuser')
