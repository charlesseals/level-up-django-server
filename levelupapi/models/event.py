from django.db import models

class Event(models.Model):
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='events')
    location = models.CharField(max_length=155)
    time = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='scheduled_events')
    con_name = models.CharField(max_length=50, default="UNKNOWN")
    attendees = models.ManyToManyField("Gamer", through='EventGamer', related_name='eventgamer_gamer')

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value