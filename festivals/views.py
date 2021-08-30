from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from festivals.models import *

# Create your views here.

class FestDetailView(DetailView):

    model = Festival

    def get_context_data(self, **kwargs):

        context = super(FestDetailView, self).get_context_data(**kwargs)
        fest = Festival.objects.get(pk = self.kwargs['pk'])
        context['fest'] = fest
        try:
            context['photos'] = Photos.objects.get(fest = fest)
        except:
            context['photos'] = []
        try:
            context['carousel'] = CarouselPhotos.objects.get(fest = fest)
        except:
            context['carousel'] = None
        return context
