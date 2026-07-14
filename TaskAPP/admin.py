from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from unfold.admin import ModelAdmin


from .models import *

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
    )


@admin.register(Task)
class TaskAdmin(ModelAdmin):
    list_display = ["id", "Title", "Assigned_To", "Status" , "manager_username"]

    @admin.display(description="Manager")
    def manager_username(self, obj):
        return obj.user.username