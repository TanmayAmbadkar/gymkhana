from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Committee(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, primary_key=True)
    logo = models.ImageField(upload_to="logos/", null = True, blank=True)
    about = models.TextField()
    achievement = models.TextField(blank=True, null=True)
    mail = models.EmailField(null = True, blank=True)

    def __str__(self):
        return self.name

class CommitteeEvent(models.Model):

    name = models.CharField(max_length=255)
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE)
    description = models.TextField()
    logo = models.ImageField(upload_to="logos/", null = True, blank=True)
    
    def __str__(self):
        return self.name

class Member(models.Model):

    committee = models.OneToOneField(Committee, on_delete=models.CASCADE)
    current = models.FileField(upload_to="csv/", blank=True)
    past = models.FileField(upload_to="csv/", blank=True)

    def __str__(self):
        return self.committee.name

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
    committee = models.OneToOneField(Committee, on_delete=models.CASCADE)

    def __str__(self):
        return self.committee.name

class CarouselPhotos(models.Model):

    photo1 = models.ImageField(blank=True, upload_to="carouselphotos/")
    photo2 = models.ImageField(blank=True, upload_to="carouselphotos/")
    photo3 = models.ImageField(blank=True, upload_to="carouselphotos/")
    committee = models.OneToOneField(Committee, on_delete=models.CASCADE)

    def __str__(self):
        return self.committee.name

class President(models.Model):

    name = models.CharField(max_length=255)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    committee = models.OneToOneField(Committee, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="profile_photo/", null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.committee.name}"

class VicePresident(models.Model):

    name = models.CharField(max_length=255)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    committee = models.OneToOneField(Committee, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="profile_photo/", null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.committee.name}"

class PIC(models.Model):

    name = models.CharField(max_length=255)
    committee = models.OneToOneField(Committee, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="profile_photo/", null=True, blank=True)
    url = models.URLField()

    def __str__(self):
        return f"{self.name} {self.committee.name}"

class CalendarEvent(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.committee.name}"
