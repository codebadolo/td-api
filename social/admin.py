# social/admin.py
from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['event', 'user', 'text', 'created_at']
    search_fields = ['event__title', 'user__username']
    list_filter = ['created_at']

# Register other models if needed
from .models import Like

admin.site.register(Like)
