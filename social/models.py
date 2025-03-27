# social/models.py
from django.db import models

class Comment(models.Model):
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

class Like(models.Model):
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'user')
