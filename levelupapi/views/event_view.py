"""View module for handling requests about events"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event


class EventView(ViewSet):
    """Level up events view"""

    def retrieve(self, request, pk):
        game_type = Event.objects.get(pk=pk)
        serializer = EventSerializer(game_type)
        return Response(serializer.data)
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """


    def list(self, request):
        game_types = Event.objects.all()
        serializer = EventSerializer(game_types, many=True)
        return Response(serializer.data)
        """Handle GET requests to get all events

        Returns:
            Response -- JSON serialized list of events
        """


class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events"""

    class Meta:
        model = Event
        fields = ('id', 'organizer', 'location', 'time', 'game', 'name')