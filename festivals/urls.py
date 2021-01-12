from django.urls import path
from festivals.views import *
from django.conf.urls import include


urlpatterns = [

    path('<str:pk>/', FestDetailView.as_view(), name="festival_detail"),
]
