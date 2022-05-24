from django.contrib import admin

from auth_.models import Profile
from main.models import User

admin.site.register(Profile)

@admin.register(User)
class UserAdminPanel(admin.ModelAdmin):
    list_display = ("login", "first_name", "last_name")
    list_filter = ("login", "first_name", "last_name")
    search_fields = ["login", "first_name", "last_name"]