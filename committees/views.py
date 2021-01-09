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
from committees.models import *

# Create your views here

class CommitteeDetailView(DetailView):

    model = Committee

    def get_context_data(self, **kwargs):

        context = super(CommitteeDetailView, self).get_context_data(**kwargs)
        committee = Committee.objects.get(pk = self.kwargs['pk'])
        context['Committee'] = committee
        #context['events'] = CommitteeEvent.objects.filter(committee = committee)
        #context['pic'] = PIC.objects.get(committee=committee)
        #context['photos'] = Photos.objects.get(committee = committee)
        #context['carousel'] = CarouselPhotos.objects.get(committee = committee)
        try:
            context['events'] = CommitteeEvent.objects.filter(committee = committee)
        except CommitteeEvent.DoesNotExist:
            context['events'] = None
        try:
            context['pic'] = PIC.objects.get(committee = committee)
        except PIC.DoesNotExist:
            context['pic'] = None
        try:
            context['photos'] = Photos.objects.get(committee = committee)
        except Photos.DoesNotExist:
            context['photos'] = None
        try:
            context['carousel'] = CarouselPhotos.objects.get(committee = committee)
        except CarouselPhotos.DoesNotExist:
            context['carousel'] = None
        try:
            context['president'] = President.objects.get(committee = committee)
        except President.DoesNotExist:
            context['president'] = None
        try:
            context['vpres'] = VicePresident.objects.get(committee = committee)
        except VicePresident.DoesNotExist:
            context['vpres'] = None
        try:
            context['clubs'] = Club.objects.filter(committee = committee).order_by("slug")
        except Club.DoesNotExist:
            context['clubs'] = None
        #context['clubs'] = Club.objects.filter(committee = committee).order_by("slug")

        try:
            member = Member.objects.get(committee = committee)
            df = pd.read_csv(member.current)
            context['curr_mem'] = get_current_members(df)
        except Member.DoesNotExist:
            context['curr_mem'] = None

        #member = Member.objects.get(committee = committee)
        #df = pd.read_csv(member.current)
        #context['curr_mem'] = get_current_members(df)

        return context

class PastMembersView(DetailView):

    model = Committee
    template_name = 'committees/past_members.html'

    def get_context_data(self, **kwargs):

        context = super(PastMembersView, self).get_context_data(**kwargs)

        committee = Committee.objects.get(pk = self.kwargs['pk'])
        member = Member.objects.get(committee = committee)
        df = pd.read_csv(member.past)

        context['members'] = get_past_members(df)

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
