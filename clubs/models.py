from django.db import models
from django.contrib.auth.models import User
from committees.models import *
# Create your models here.
class Club(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, primary_key=True)
    logo = models.ImageField(upload_to="logos/", null = True, blank=True)
    about = models.TextField()
    achievements = models.TextField()
    mail = models.EmailField(null = True, blank=True)
    linkedin = models.URLField(null = True, blank=True)
    github = models.URLField(null = True, blank=True)
    instagram = models.URLField(null = True, blank=True)
    facebook = models.URLField(null = True, blank=True)
    twitter = models.URLField(null = True, blank=True)
    dribble = models.URLField(null = True, blank=True)
    youtube = models.URLField(null = True, blank=True)
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class ClubEvent(models.Model):

    name = models.CharField(max_length=255)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    description = models.TextField()


    def __str__(self):
        return self.name

class Photos(models.Model):

    photo1 = models.ImageField(blank=True, upload_to="clubphotos/")
    caption1 = models.CharField(max_length=255, null=True)
    photo2 = models.ImageField(blank=True, upload_to="clubphotos/")
    caption2 = models.CharField(max_length=255, null=True)
    photo3 = models.ImageField(blank=True, upload_to="clubphotos/")
    caption3 = models.CharField(max_length=255, null=True)
    photo4 = models.ImageField(blank=True, upload_to="clubphotos/")
    caption4 = models.CharField(max_length=255, null=True)
    photo5 = models.ImageField(blank=True, upload_to="clubphotos/")
    caption5 = models.CharField(max_length=255, null=True)
    photo6 = models.ImageField(blank=True, upload_to="clubphotos/")
    caption6 = models.CharField(max_length=255, null=True)
    photo7 = models.ImageField(blank=True, upload_to="clubphotos/")
    caption7 = models.CharField(max_length=255, null=True)
    photo8 = models.ImageField(blank=True, upload_to="clubphotos/")
    caption8 = models.CharField(max_length=255, null=True)
    photo9 = models.ImageField(blank=True, upload_to="clubphotos/")
    caption9 = models.CharField(max_length=255, null=True)
    club = models.OneToOneField(Club, on_delete=models.CASCADE)

    def __str__(self):
        return self.club.name

class CarouselPhotos(models.Model):

    photo1 = models.ImageField(blank=True, upload_to="carouselphotos/")
    photo2 = models.ImageField(blank=True, upload_to="carouselphotos/")
    photo3 = models.ImageField(blank=True, upload_to="carouselphotos/")
    club = models.OneToOneField(Club, on_delete=models.CASCADE)

    def __str__(self):
        return self.club.name

class Secretary(models.Model):

    name = models.CharField(max_length=255)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    dribble = models.URLField(null = True, blank=True)
    club = models.OneToOneField(Club, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="profile_photo/", null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.club.name}"

class JointSecretary(models.Model):

    name = models.CharField(max_length=255)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    dribble = models.URLField(null = True, blank=True)
    club = models.OneToOneField(Club, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="profile_photo/", null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.club.name}"

class Members(models.Model):

    club = models.OneToOneField(Club, on_delete=models.CASCADE)
    past = models.FileField(upload_to="csv/")

    def __str__(self):

        return self.club.name

class CalendarEvent(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.club.name}"
