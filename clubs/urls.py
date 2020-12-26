from django.urls import path
from clubs.views import *
from django.conf.urls import include


urlpatterns = [
    path('<str:pk>/', ClubDetailView.as_view(), name="club_detail"),
    path('<str:pk>/past_members', PastMembersView.as_view(), name="past_club")
]
