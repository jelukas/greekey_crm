from django.contrib import admin
from .models import Project, Milestone, Task, TaskTimer


admin.site.register(Project)
admin.site.register(Milestone)
admin.site.register(Task)
admin.site.register(TaskTimer)