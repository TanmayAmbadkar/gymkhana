from django.shortcuts import render
from django.views.generic import TemplateView
from clubs.models import CalendarEvent as ClubEvent
from committees.models import CalendarEvent as CommitteeEvent
from django.http import JsonResponse
# Create your views here.

def get_dates(request):

    weekdays = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri", 5: "Sat", 6: "Sun"}
    clubevents = ClubEvent.objects.all()
    comevents = CommitteeEvent.objects.all()
    globalEventObject = {}
    for event in clubevents:
        weekday = weekdays[event.start_date.weekday()]
        month = event.start_date.strftime("%b")
        year,day = str(event.start_date).split('-')[0], str(event.start_date).split('-')[2]
        date = f"{weekday} {month} {day} {year}"

        if date not in globalEventObject:
            globalEventObject[date] = {}

        globalEventObject[date][event.name+" start"] = event.description

        weekday = weekdays[event.end_date.weekday()]
        month = event.end_date.strftime("%b")
        year,day = str(event.end_date).split('-')[0], str(event.end_date).split('-')[2]
        date = f"{weekday} {month} {day} {year}"

        if date not in globalEventObject:
            globalEventObject[date] = {}

        globalEventObject[date][event.name+" end"] = event.description

    for event in comevents:
        weekday = weekdays[event.start_date.weekday()]
        month = event.start_date.strftime("%b")
        year,day = str(event.start_date).split('-')[0], str(event.start_date).split('-')[2]
        date = f"{weekday} {month} {day} {year}"

        if date not in globalEventObject:
            globalEventObject[date] = {}

        globalEventObject[date][event.name+" start"] = event.description

        weekday = weekdays[event.end_date.weekday()]
        month = event.end_date.strftime("%b")
        year,day = str(event.end_date).split('-')[0], str(event.end_date).split('-')[2]
        date = f"{weekday} {month} {day} {year}"

        if date not in globalEventObject:
            globalEventObject[date] = {}

        globalEventObject[date][event.name+" end"] = event.description


    return JsonResponse(globalEventObject)

class CalendarView(TemplateView):

    template_name="schedule/calendar.html"
