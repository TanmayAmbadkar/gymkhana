from django.shortcuts import render
from django.views.generic import TemplateView
from homepage.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

        return context
