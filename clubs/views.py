from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateResponseMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.core import serializers
from django.http import HttpResponse
import pandas as pd
from clubs.models import *

# Create your views here.
class ClubDetailView(DetailView):

    model = Club

    def get_context_data(self, **kwargs):

        context = super(ClubDetailView, self).get_context_data(**kwargs)
        club = Club.objects.get(pk = self.kwargs['pk'])
        context['club'] = club
        #context['events'] = ClubEvent.objects.filter(club = club)
        #context['photos'] = Photos.objects.get(club = club)
        #context['carousel'] = CarouselPhotos.objects.get(club = club)
        try:
            context['carousel'] = CarouselPhotos.objects.get(club=club)
        except CarouselPhotos.DoesNotExist:
            context['carousel'] = None
        try:
            context['photos'] = Photos.objects.get(club=club)
        except Photos.DoesNotExist:
            context['photos'] = None
        try:
            context['events'] = ClubEvent.objects.filter(club=club)
        except ClubEvent.DoesNotExist:
            context['events'] = None
        #context['sec'] = Secretary.objects.get(club = club)
        #context['jsec'] = JointSecretary.objects.get(club = club)
        try:
            context['sec'] = Secretary.objects.get(club=club)
        except Secretary.DoesNotExist:
            context['sec'] = None

        try:
            context['jsec'] = JointSecretary.objects.get(club=club)
        except JointSecretary.DoesNotExist:
            context['jsec'] = None

        return context

class PastMembersView(DetailView):

    model = Club
    template_name = 'clubs/past_members.html'

    def get_context_data(self, **kwargs):

        context = super(PastMembersView, self).get_context_data(**kwargs)

        club = Club.objects.get(pk = self.kwargs['pk'])
        member = Members.objects.get(club = club)
        df = pd.read_csv(member.past)

        context['members'] = get_past_members(df)

        return context

def get_past_members(df):

    values = []
    for i in range(len(df)):
        row={}
        row['serial'] = i+1
        row['name'] = df['Name'][i]
        row['batch'] = df['Batch'][i]
        row['position'] = df['Position'][i]
        row['from'] = df['From'][i]
        values.append(row)

    return values
