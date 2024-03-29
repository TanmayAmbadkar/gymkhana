from django.urls import path
from homepage.views import *
from django.conf.urls import include

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('contact', ContactView.as_view(), name="contact"),
    path('event', get_event, name="get_event"),
    path('contributors', ContributorView.as_view(), name="contributors"),
]
