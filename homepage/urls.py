from django.urls import path
from homepage.views import *
from django.conf.urls import include

urlpatterns = [
    path('', HomeView.as_view(), name="home")
]
