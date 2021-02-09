from django.shortcuts import render
from django.views.generic import TemplateView
from homepage.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from committees.models import Committee, PIC
from clubs.models import Club
from django.http import JsonResponse
# Create your views here.


class HomeView(TemplateView):

    template_name = 'homepage/home.html'

    def get_context_data(self, **kwargs):

        context = super(TemplateView, self).get_context_data(**kwargs)

        announcements = Update.objects.filter(type="Announcements").filter(published=True).order_by('-created_date')
        news = Update.objects.filter(type="News").filter(published=True).order_by('-created_date')
        context['announcements'] = announcements
        context['news'] = news
        context['main_image'] = MainPhoto.objects.first()
        context['about'] = About.objects.first()
        context['countdown'] = Countdown.objects.first()

        return context

class ContactView(TemplateView):

    template_name = 'homepage/contact.html'

    def get_context_data(self, **kwargs):

        context = super(ContactView, self).get_context_data(**kwargs)

        context['profs'] = PIC.objects.all()
        context['committees'] = Committee.objects.all().order_by('slug')
        context['clubs'] = Club.objects.all().order_by('slug')

        return context

def get_event(request):

    weekdays = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri", 5: "Sat", 6: "Sun"}
    event = Countdown.objects.first()
    date = event.date
    name = event.event_name

    month = date.strftime("%b")
    year = date.strftime("%Y")
    day = date.strftime("%d")
    date = f"{month} {day}, {year} {date.strftime('%H:%M:%S')}"
    print(day)

    return JsonResponse({"name": name, 'dt': date})
