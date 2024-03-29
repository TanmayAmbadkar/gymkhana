from django.contrib import admin
from gallery.models import *
from committees.models import *
from clubs.models import *

# Register your models here.
class EventAdmin(admin.ModelAdmin):

    def get_queryset(self, request):

        qs = super(EventAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        if Committee.objects.get(user = request.user):
            return qs.filter(committee=Committee.objects.get(user = request.user))

        elif Club.objects.get(user = request.user):
            return qs.filter(club=Club.objects.get(user = request.user))

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            return super(EventAdmin, self).get_form(request, obj, **kwargs)

        if Committee.objects.get(user = request.user):
            self.exclude = ('club', 'committee')

        elif Club.objects.get(user = request.user):
            self.exclude = ('committee', 'club')
        form = super(EventAdmin, self).get_form(request, obj, **kwargs)
        return form

    def save_model(self, request, obj, form, change):

        committee = Committee.objects.get(user=request.user)
        obj.committee = committee
        super().save_model(request, obj, form, change)



admin.site.register(Photo)
admin.site.register(Event, EventAdmin)
