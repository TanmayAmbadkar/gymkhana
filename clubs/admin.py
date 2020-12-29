from django.contrib import admin
from clubs.models import *
# Register your models here.

class ClubAdmin(admin.ModelAdmin):

    def get_queryset(self, request):

        qs = super(ClubAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        club = Club.objects.get(user=request.user)
        print(club)
        return qs.filter(user=request.user)

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            return super(ClubAdmin, self).get_form(request, obj, **kwargs)

        self.exclude = ('user', 'slug', 'committee')
        form = super(ClubAdmin, self).get_form(request, obj, **kwargs)
        return form


class FieldsAdmin(admin.ModelAdmin):

    def get_queryset(self, request):

        qs = super(FieldsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        club = Club.objects.get(user=request.user)
        return qs.filter(club = club)

admin.site.register(Club, ClubAdmin)
admin.site.register(ClubEvent, FieldsAdmin)
admin.site.register(Photos, FieldsAdmin)
admin.site.register(CarouselPhotos, FieldsAdmin)
admin.site.register(Secretary, FieldsAdmin)
admin.site.register(JointSecretary, FieldsAdmin)
admin.site.register(Members, FieldsAdmin)
admin.site.register(CalendarEvent, FieldsAdmin)
