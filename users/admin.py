# users/admin.py
from django.contrib import admin
from .models import User
# users/admin.py
from django.contrib import admin
from .models import UserProfile
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'date_joined']
    search_fields = ['username', 'email']
    list_filter = ['is_active', 'date_joined']


# users/admin.py
from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'display_interests']  # Use a custom method for Many-to-Many fields

    def display_interests(self, obj):
        return ", ".join([interest.name for interest in obj.interests.all()])
    display_interests.short_description = "Interests"  # Column header name
