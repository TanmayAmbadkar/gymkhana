from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Update(models.Model):

    choices = [('Announcements', 'Announcements'), ('News', 'News')]
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=choices)
    created_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    pdf = models.FileField(upload_to = "pdf/", null=True, blank=True)
    youtube_id = models.CharField(blank=True, null=True, max_length=20)

    def __str__(self):
        return f"{self.title} {self.created_date.date()} {self.type} {'published' if self.published else 'not published'}"

class MainPhoto(models.Model):

    url = models.URLField()

    def __str__(self):
        return self.url

class About(models.Model):

    description = models.TextField()
