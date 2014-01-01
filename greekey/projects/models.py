from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from contacts.models import Contact


class ProjectStatus(models.Model):
	name = models.CharField(max_length=230)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name


class Project(models.Model):
	title = models.CharField(max_length=230)
	description = models.TextField(blank=True)
	contact = models.ForeignKey(Contact, related_name='projects')
	members = models.ManyToManyField(User, related_name='projects')
	status = models.ForeignKey(ProjectStatus, default=1)

	def __unicode__(self):
		return self.title + ' ' + str(self.contact)

	def __str__(self):
		return self.title + ' ' + str(self.contact)



class Task(MPTTModel):
	created =  models.DateTimeField(auto_now_add=True)
	modified =  models.DateTimeField(auto_now=True)
	project = models.ForeignKey('Project', related_name='tasks')
	asiggned_to = models.ManyToManyField(User, related_name='tasks')
	description = models.TextField()
	completed_prevission = models.DateTimeField()
	completed_datetime = models.DateTimeField(blank=True, null=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

	def __unicode__(self):
		return self.description

	def __str__(self):
		return self.description

	class MPTTMeta:
	        order_insertion_by = ['created']


class TaskTimer(models.Model):
	start_time = models.DateTimeField()
	stop_time = models.DateTimeField(blank=True, null=True)
	user = models.ForeignKey(User, related_name='tasks_timers')
	task = models.ForeignKey(Task, related_name='timers')

	def __unicode__(self):
		return str(self.user) + ' - ' + str(self.task) + ' - Time: ' + str(self.start_time) + ' ' + str(self.stop_time)

	def __str__(self):
		return  str(self.user) + ' - ' + str(self.task) + ' - Time: ' + str(self.start_time) + ' ' + str(self.stop_time)