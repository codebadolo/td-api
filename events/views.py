from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event, EventImage
from .serializers import EventSerializer

class EventListView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        images = request.FILES.getlist('images')  # Get uploaded images

        event_serializer = EventSerializer(data=data)
        if event_serializer.is_valid():
            event = event_serializer.save()

            # Save uploaded images
            for image in images:
                EventImage.objects.create(event=event, image=image)

            return Response(event_serializer.data, status=status.HTTP_201_CREATED)
        return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
