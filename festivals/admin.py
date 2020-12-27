from django.contrib import admin
from festivals.models import *
# Register your models here.

class FestAdmin(admin.ModelAdmin):

    def get_queryset(self, request):

        qs = super(FestAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(user=request.user)

    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            return super(FestAdmin, self).get_form(request, obj, **kwargs)

        self.exclude = ('user', )
        form = super(FestAdmin, self).get_form(request, obj, **kwargs)
        return form


class FieldsAdmin(admin.ModelAdmin):

    def get_queryset(self, request):

        qs = super(FieldsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        fest = Festival.objects.get(user=request.user)
        return qs.filter(fest = fest)

admin.site.register(Festival, FestAdmin)
admin.site.register(Photos, FieldsAdmin)
admin.site.register(CarouselPhotos, FieldsAdmin)
