from django.db import models

class Event(models.Model):
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='events')
    location = models.CharField(max_length=155)
    time = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='scheduled_events')