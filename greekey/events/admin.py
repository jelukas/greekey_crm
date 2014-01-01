from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
	list_display = ['datetime','type','from_user','to_contact','subject']


admin.site.register(Event, EventAdmin)