from django.contrib import admin

# Register your models here.
from django.contrib import admin
from committees.models import *
# Register your models here.

admin.site.register(Committee)
admin.site.register(CommitteeEvent)
admin.site.register(Photos)
admin.site.register(CarouselPhotos)
admin.site.register(CommitteeAdmin)
admin.site.register(President)
admin.site.register(Member)
admin.site.register(PIC)
admin.site.register(CalendarEvent)
