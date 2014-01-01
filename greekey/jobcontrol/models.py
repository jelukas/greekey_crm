import datetime
from django.db import models
from django.contrib.auth.models import User


class GeneralTimerRegistry(models.Model):
	start_working = models.DateTimeField(auto_now_add=True)
	end_working = models.DateTimeField(blank=True, null=True)
	duration = models.TimeField(blank=True, null=True, verbose_name='Time') # In minutes
	worker = models.ForeignKey(User, related_name='general_timers')
	
	class Meta:
		ordering = ['-start_working']

	def save(self, *args, **kwargs):
		if self.id and self.end_working != None:
			elapsedTime = self.end_working - self.start_working
			self.duration =  str(elapsedTime)
		super(GeneralTimerRegistry,self).save(*args, **kwargs)


	@classmethod
	def get_month_working_time_by_user(self, user, month, year):
		from datetime import timedelta
		totaltime = timedelta(seconds=0)
		timers = self.objects.filter(start_working__year=year, start_working__month=month, worker=user).exclude(end_working__isnull=True)
		for timer in timers:
			totaltime += timedelta(hours=timer.duration.hour, minutes=timer.duration.minute, seconds = timer.duration.second)
		return totaltime

