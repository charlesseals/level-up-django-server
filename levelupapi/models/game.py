from django.db import models

class Game(models.Model):
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='created_games')
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE,related_name='games')
    designer = models.CharField(max_length=40)
    number_of_players = models.IntegerField(default=1)
    skill_level = models.CharField(default="medium", max_length=15)