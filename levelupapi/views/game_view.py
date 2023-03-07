"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game, Gamer, GameType


class GameView(ViewSet):
    """Level up games view"""

    def retrieve(self, request, pk):
        try:
            game_type = Game.objects.get(pk=pk)
            serializer = GameSerializer(game_type)
            return Response(serializer.data)
        except Exception as ex:
            return Response({"Message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
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


    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        gamer = Gamer.objects.get(user=request.auth.user)
        game_type = GameType.objects.get(pk=request.data["game_type"])

        game = Game.objects.create(
            gamer=gamer,
            title=request.data["title"],
            description=request.data["description"],
            game_type=game_type,
            designer=request.data["designer"],
            number_of_players=request.data["number_of_players"],
            skill_level=request.data["skill_level"]
        )
        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # try:
        #     description=request.data["description"]
        # except:
        #     description=None


    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        game = Game.objects.get(pk=pk)
        game.title = request.data["title"]
        game.designer = request.data["designer"]
        game.number_of_players = request.data["number_of_players"]
        game.skill_level = request.data["skill_level"]
        game.description = request.data["description"]

        game_type = GameType.objects.get(pk=request.data["game_type"])
        game.game_type = game_type
        game.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


    def destroy(self, request, pk):
        game = Game.objects.get(pk=pk)
        game.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
            

class GamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamer
        fields = ('id', 'user', 'bio')

class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    gamer = GamerSerializer(many=False)
    
    class Meta:
        model = Game
        fields = ('id', 'gamer', 'title', 'description', 'game_type', 'designer', 'number_of_players', 'skill_level')
        depth = 1