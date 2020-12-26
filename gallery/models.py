from django.db import models
from committees.models import Committee
from clubs.models import Club
# Create your models here.

class Event(models.Model):

    name = models.CharField(max_length=200)
    club = models.ForeignKey(Club, blank=True, null=True, on_delete=models.CASCADE)
    committee = models.ForeignKey(Committee, blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.name

class Photo(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="eventphotos/")
    caption = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.event} {self.pk}"
