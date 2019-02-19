from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return "Room %s" % (self.name)

class Reservation(models.Model):
    room = models.ForeignKey(Room, models.CASCADE)
    organisor = models.ForeignKey(get_user_model(), models.CASCADE)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    @property
    def duration(self):
        duration = enddate - startdate
        return duration.total_seconds()
    
    def __str__(self):
        return "Reservation for %s starting %s" % (self.room.name, self.startdate)
