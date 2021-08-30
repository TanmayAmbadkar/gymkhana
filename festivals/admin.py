from django.contrib import admin
from festivals.models import *
from committees.models import Committee
# Register your models here.

class FestAdmin(admin.ModelAdmin):

    def get_queryset(self, request):

        qs = super(FestAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        committee = Committee.objects.get(user=request.user)
        return qs.filter(committee=committee)

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            return super(FestAdmin, self).get_form(request, obj, **kwargs)

        self.exclude = ('slug', 'committee')
        form = super(FestAdmin, self).get_form(request, obj, **kwargs)
        return form

    def save_model(self, request, obj, form, change):

        if request.user.is_superuser:
            super().save_model(request, obj, form, change)
            return

        committee = Committee.objects.get(user=request.user)
        obj.committee = committee
        super().save_model(request, obj, form, change)


class FieldsAdmin(admin.ModelAdmin):

    def get_queryset(self, request):

        qs = super(FieldsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        committee = Committee.objects.get(user=request.user)
        fest = Festival.objects.get(committee=committee)
        return qs.filter(fest = fest)

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            return super(FieldsAdmin, self).get_form(request, obj, **kwargs)

        self.exclude = ('fest', )
        form = super(FieldsAdmin, self).get_form(request, obj, **kwargs)
        return form

    def save_model(self, request, obj, form, change):

        if request.user.is_superuser:
            super().save_model(request, obj, form, change)
            return

        committee = Committee.objects.get(user=request.user)
        fest = Festival.objects.get(committee=committee)
        obj.fest = fest
        super().save_model(request, obj, form, change)

admin.site.register(Festival, FestAdmin)
admin.site.register(Photos, FieldsAdmin)
admin.site.register(CarouselPhotos, FieldsAdmin)
