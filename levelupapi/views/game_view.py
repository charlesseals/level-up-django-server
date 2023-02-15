"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game


class GameView(ViewSet):
    """Level up games view"""

    def retrieve(self, request, pk):
        game_type = Game.objects.get(pk=pk)
        serializer = GameSerializer(game_type)
        return Response(serializer.data)
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game
        """


    def list(self, request):
        game_types = Game.objects.all()
        serializer = GameSerializer(game_types, many=True)
        return Response(serializer.data)
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """


class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    class Meta:
        model = Game
        fields = ('id', 'gamer', 'name', 'description', 'game_type', 'designer', 'number_of_players', 'skill_level')