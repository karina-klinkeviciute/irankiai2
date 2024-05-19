from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User

# Register your models here.


class MyUserAdmin(UserAdmin):
    list_display = ("email", "first_name", "last_name", "is_staff", "is_active", "is_superuser")


admin.site.register(User, MyUserAdmin)
