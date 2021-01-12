from django.urls import path
from schedule.views import *


urlpatterns = [
    path('dates', get_dates, name="get_dates"),
    path('', CalendarView.as_view(), name="calendar"),
]
