"""View module for handling requests about events"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Gamer, Game
from rest_framework.decorators import action


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


    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        organizer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data['game'])

        # try:
        #     description=request.data["description"]
        # except:
        #     description=None

        event = Event.objects.create(
            organizer=organizer,
            location=request.data["location"],
            time=request.data["time"],
            game=game,
            con_name=request.data["con_name"]
        )
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        gamer = Gamer.objects.get(user=request.auth.user)
        event = Event.objects.get(pk=pk)
        event.con_name = request.data["con_name"]
        event.location = request.data["location"]
        event.organizer = gamer
        event.time = request.data["time"]

        game = Game.objects.get(pk=request.data["game"])
        event.game = game
        event.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


    def destroy(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamer
        fields = ('full_name', )

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events"""
    organizer = OrganizerSerializer(many=False)
    class Meta:
        model = Event
        fields = ('id', 'organizer', 'location', 'time', 'game', 'con_name')
        