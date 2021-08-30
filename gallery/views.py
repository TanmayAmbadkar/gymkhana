from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from gallery.models import *

# Create your views here.

class GalleryView(TemplateView):

    template_name = "gallery/gallery.html"

    def get_context_data(self, **kwargs):

        context = super(GalleryView, self).get_context_data(**kwargs)

        l = []
        for event in Event.objects.all().order_by('-date'):

            if len(Photo.objects.filter(event=event))==0:
                continue
            d = {}
            d['name'] = event.name
            d['ename'] = ''.join(event.name.split())
            d['photos'] = Photo.objects.filter(event=event)
            l.append(d)

        context['events'] = l

        return context
