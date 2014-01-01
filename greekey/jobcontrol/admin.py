from django.contrib import admin
from .models import GeneralTimerRegistry


class GeneralTimerRegistryAdmin(admin.ModelAdmin):
	fields = ['start_working','end_working','duration','worker']
	readonly_fields = ['start_working','duration']
	list_display = ['start_working','end_working','duration','worker']


admin.site.register(GeneralTimerRegistry,GeneralTimerRegistryAdmin)
