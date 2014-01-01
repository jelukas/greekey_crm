from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from contacts.models import Contact
from projects.models import Project


EVENT_TYPES = (
	('phonecall','Phone Call'),
	('email','Email'),
	('metting','Metting'),
)

class Event(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	datetime = models.DateTimeField(default=datetime.now())
	from_user = models.ForeignKey(User, related_name='events')
	to_contact = models.ForeignKey(Contact, related_name='events', blank=True, null=True)
	project_related = models.ForeignKey(Project, related_name='events', blank=True, null=True)
	type = models.CharField(max_length=250, choices=EVENT_TYPES)
	subject = models.CharField(max_length=250)
	description = models.TextField(blank=True)