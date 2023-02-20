# """View module for handling requests about games"""
# from django.http import HttpResponseServerError
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from rest_framework import serializers, status
# from levelupapi.models import Game, Gamer, GameType


# class GamerView(ViewSet):
#     """Level up gamers view"""

#     def retrieve(self, request, pk):
#         gamer_type = Gamer.objects.get(pk=pk)
#         serializer = GamerSerializer(gamer_type)
#         return Response(serializer.data)
#         """Handle GET requests for single gamer

#         Returns:
#             Response -- JSON serialized gamer
#         """


#     def list(self, request):
#         gamer_types = Gamer.objects.all()
#         serializer = GamerSerializer(gamer_types, many=True)
#         return Response(serializer.data)
#         """Handle GET requests to get all gamers

#         Returns:
#             Response -- JSON serialized list of gamers
#         """


#     def create(self, request):
#         """Handle POST operations

#         Returns
#             Response -- JSON serialized gamer instance
#         """
#         gamerr = Gamerr.objects.get(user=request.auth.user)
#         gamer_type = GamerType.objects.get(pk=request.data["gamer_type"])

#         # try:
#         #     description=request.data["description"]
#         # except:
#         #     description=None

#         gamer = Gamer.objects.create(
#             gamerr=gamerr,
#             title=request.data["title"],
#             description=request.data["description"],
#             gamer_type=gamer_type,
#             designer=request.data["designer"],
#             number_of_players=request.data["number_of_players"],
#             skill_level=request.data["skill_level"]
#         )
#         serializer = GamerSerializer(gamer)
#         return Response(serializer.data)


# class GamerSerializer(serializers.ModelSerializer):
#     """JSON serializer for gamers
#     """
#     class Meta:
#         model = Gamer
#         fields = ('id', 'gamerr', 'title', 'description', 'gamer_type', 'designer', 'number_of_players', 'skill_level')
#         depth = 1