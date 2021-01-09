from django.urls import path
from committees.views import *
from django.conf.urls import include


urlpatterns = [

    path('<str:pk>/', CommitteeDetailView.as_view(), name="committee_detail"),
    path('<str:pk>/past_members/', PastMembersView.as_view(), name="past_members"),
    path('<str:pk>/curr_members/', CurrentMembersView.as_view(), name="curr_members")
]
