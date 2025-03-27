# recommendations/models.py
from django.db import models

class UserEventInteraction(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=20, choices=[
        ('view', 'View'),
        ('attend', 'Attend'),
        ('share', 'Share')
    ])
    timestamp = models.DateTimeField(auto_now_add=True)
