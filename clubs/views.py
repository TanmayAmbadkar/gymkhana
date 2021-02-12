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
            context['upcoming'] = ClubEvent.objects.filter(club = club).filter(upcoming=True)
            context['major_events'] = ClubEvent.objects.filter(club = club).filter(upcoming=False)
        except ClubEvent.DoesNotExist:
            context['major_events'] = None
            context['present_events'] = None
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

class CurrentMembersView(DetailView):

    model = Club
    template_name = 'clubs/current_members.html'

    def get_context_data(self, **kwargs):

        context = super(CurrentMembersView, self).get_context_data(**kwargs)

        club = Club.objects.get(pk = self.kwargs['pk'])
        member = Members.objects.get(club = club)
        df = pd.read_csv(member.curr)

        context['members'] = get_current_members(df)
        return context


def get_current_members(df):

    values = []
    for i in range(len(df)):
        row={}
        row['serial'] = i+1
        row['name'] = df['Name'][i]
        row['batch'] = df['Batch'][i]
        row['position'] = df['Position'][i]
        values.append(row)

    return values

def get_past_members(df):

    values = {}
    for i in range(len(df)):
        row={}

        row['name'] = df['Name'][i]
        row['batch'] = df['Batch'][i]
        row['position'] = df['Position'][i]

        if df['From'][i] not in values:
            values[ df['From'][i]] = []

        x = len(values[ df['From'][i]])
        row['serial'] = x+1
        values[df['From'][i]].append(row)

    sheets = []
    i = 0
    keys = list(values.keys())
    keys.sort()
    for key in keys:
        sheet = {'year': key}
        sheet['df'] = values[key]
        if i==0:
            sheet['active'] = 'active'
        sheets.append(sheet)
        i+=1

    return sheets
