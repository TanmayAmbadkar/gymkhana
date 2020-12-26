from django.urls import path
from gallery.views import *


urlpatterns = [
    path('', GalleryView.as_view(), name="gallery"),

]
