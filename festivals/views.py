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
        context['photos'] = Photos.objects.get(fest = fest)
        context['carousel'] = CarouselPhotos.objects.get(fest = fest)
        return context
