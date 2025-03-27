# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    following = models.ManyToManyField('self', symmetrical=False, blank=True)
    interests = models.ManyToManyField('events.Category', related_name='interested_users')
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
