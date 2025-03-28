from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import  Event


@login_required
def user_events(request):
    events = Event.objects.filter(organizer=request.user)
    data = [{'title': event.title, 'date': event.date} for event in events]
    return JsonResponse(data, safe=False)
