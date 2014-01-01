from django.contrib import admin
from .models import Project, Task, TaskTimer


class TaskTimerAdmin(admin.ModelAdmin):
	list_display = ['task','user','start_time','stop_time']


admin.site.register(Project)
admin.site.register(Task)
admin.site.register(TaskTimer,TaskTimerAdmin)