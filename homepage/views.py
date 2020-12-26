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
        paginator_announcements = Paginator(announcements, 3)
        paginator_news = Paginator(news, 3)
        news_page_number = self.request.GET.get('news')
        announcement_page_number = self.request.GET.get('ann')

        try:
            ann = paginator_announcements.page(announcement_page_number)
        except PageNotAnInteger:
            ann = paginator_announcements.page(1)
        except EmptyPage:
            ann = paginator_announcements.page(paginator_announcements.num_pages)

        try:
            new = paginator_news.page(news_page_number)
        except PageNotAnInteger:
            new = paginator_news.page(1)
        except EmptyPage:
            new = paginator_news.page(paginator_news.num_pages)

        context['announcements'] = ann
        context['news'] = new
        context['main_image'] = MainPhoto.objects.first()
        context['about'] = About.objects.first()

        return context
