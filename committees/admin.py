from django.contrib import admin
from committees.models import *
# Register your models here.

class CommitteeAdmin(admin.ModelAdmin):

    def get_queryset(self, request):

        qs = super(CommitteeAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        committee = Committee.objects.get(user=request.user)
        print(committee)
        return qs.filter(user=request.user)

    def get_form(self, request, obj=None, **kwargs):

        if request.user.is_superuser:
            return super(CommitteeAdmin, self).get_form(request, obj, **kwargs)

        self.exclude = ('user', 'slug')
        form = super(CommitteeAdmin, self).get_form(request, obj, **kwargs)
        return form

class FieldsAdmin(admin.ModelAdmin):

    def get_queryset(self, request):

        qs = super(FieldsAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        committee = Committee.objects.get(user=request.user)
        print(committee)
        return qs.filter(committee=committee)


admin.site.register(Committee, CommitteeAdmin)
admin.site.register(CommitteeEvent, FieldsAdmin)
admin.site.register(Photos, FieldsAdmin)
admin.site.register(CarouselPhotos, FieldsAdmin)
admin.site.register(President, FieldsAdmin)
admin.site.register(Member, FieldsAdmin)
admin.site.register(PIC, FieldsAdmin)
admin.site.register(CalendarEvent, FieldsAdmin)
