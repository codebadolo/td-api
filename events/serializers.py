from rest_framework import serializers
from .models import Event, Category, Location


from rest_framework import serializers
from .models import Event, EventImage, Category, Location

class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ['id', 'image']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'icon']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'address', 'coordinates', 'capacity']

class EventSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    location = LocationSerializer(read_only=True)
    event_images = EventImageSerializer(many=True, read_only=True)  # Use updated related_name

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'description', 'date', 'location', 
            'categories', 'organizer', 'status', 
            'created_at', 'attendees', 'event_images'
        ]
