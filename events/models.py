# events/models.py

from django.contrib.gis.db import models
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon = models.CharField(max_length=30)

class Location(models.Model):
    name = models.CharField(max_length=255 , blank = True)  # Ensure this field exists
    address = models.CharField(max_length=255)
    coordinates = models.PointField(blank = True , null = True)
    capacity = models.PositiveIntegerField(blank = True , null = True)

class Event(models.Model):
    EVENT_STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('canceled', 'Canceled'),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.PROTECT  )
    categories = models.ManyToManyField(Category)
    organizer = models.ForeignKey('users.User', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=EVENT_STATUS, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    attendees = models.ManyToManyField('users.User', related_name='attended_events', blank=True)
    class Meta:
        indexes = [
            models.Index(fields=['date', 'status']),
            models.Index(fields=['organizer']),
        ]
    
    def __str__(self):
        return self.title