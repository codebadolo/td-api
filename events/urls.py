from django.urls import path
from .views import  user_events

urlpatterns = [
  
    path('events/', user_events, name='user-events'),
]
