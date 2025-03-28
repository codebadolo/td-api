# events/admin.py
from django.contrib import admin
from .models import Event
from unfold.admin import ModelAdmin
@admin.register(Event)
class EventAdmin(ModelAdmin):
    list_display = ['title', 'date', 'organizer', 'status']
    search_fields = ['title', 'organizer__username']
    list_filter = ['status', 'date']

# Register other models if needed
from .models import Location, Category

admin.site.register(Location)
admin.site.register(Category)
