from django.db import models
from django.contrib.auth.models import User
from contacts.models import Company


class Project(models.Model):
	title = models.CharField(max_length=230)
	description = models.TextField(blank=True)
	company = models.ForeignKey(Company, related_name='projects')
	members = models.ManyToManyField(User, related_name='projects')

	def __unicode__(self):
		return self.title + ' ' + self.company

	def __str__(self):
		return self.title + ' ' + self.company


class Milestone(models.Model):
	project = models.ForeignKey(Project, related_name='milestones')
	description = models.TextField()
	completed_prevission = models.DateTimeField()
	completed_time = models.DateTimeField(blank=True, null=True)

	def __unicode__(self):
		return self.project + ' - ' + self.description

	def __str__(self):
		return self.project + ' - ' + self.description


class Task(models.Model):
	milestone = models.ForeignKey(Milestone, related_name='tasks')
	asiggned_to = models.ForeignKey(User, related_name='tasks')
	description = models.TextField()
	duration = models.IntegerField()

	def __unicode__(self):
		return self.description

	def __str__(self):
		return self.description


class TaskTimer(models.Model):
	start_time = models.DateTimeField()
	stop_time = models.DateTimeField(blank=True, null=True)
	user = models.ForeignKey(User, related_name='tasks_timers')
	task = models.ForeignKey(Task, related_name='timers')

	def __unicode__(self):
		return self.user + ' - ' + self.task + ' - Time: ' + str(self.start_time) + ' ' + str(self.stop_time)

	def __str__(self):
		return self.user + ' - ' + self.task + ' - Time: ' + str(self.start_time) + ' ' + str(self.stop_time)