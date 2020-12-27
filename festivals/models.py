from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Festival(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, primary_key=True)
    logo = models.ImageField(upload_to="logos/", null = True, blank=True)
    about = models.TextField()
    events = models.TextField()
    mail = models.EmailField(null = True, blank=True)
    url = models.URLField(null = True, blank=True)
    linkedin = models.URLField(null = True, blank=True)
    github = models.URLField(null = True, blank=True)
    instagram = models.URLField(null = True, blank=True)
    facebook = models.URLField(null = True, blank=True)
    twitter = models.URLField(null = True, blank=True)

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
    fest = models.OneToOneField(Festival, on_delete=models.CASCADE)

    def __str__(self):
        return self.fest.name

class CarouselPhotos(models.Model):

    photo1 = models.ImageField(blank=True, upload_to="carouselphotos/")
    photo2 = models.ImageField(blank=True, upload_to="carouselphotos/")
    photo3 = models.ImageField(blank=True, upload_to="carouselphotos/")
    fest = models.OneToOneField(Festival, on_delete=models.CASCADE)

    def __str__(self):
        return self.fest.name
