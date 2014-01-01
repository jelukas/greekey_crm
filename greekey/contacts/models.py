from django.db import models


MOREINFO_CHOICES = (
	('twitter', 'Twitter URL'),
	('facebook', 'Facebook URL'),
	('phone', 'Phone Number'),
	('website', 'Website'),
	('googleplus', 'Google Plus URL'),
	('email', 'Email Address'),
)

CONTACT_TYPE_CHOICES = (
	('company', 'Company'),
	('person', 'Individual Person'),
)


class Contact(models.Model):
	firstname = models.CharField(max_length=250)
	lastname = models.CharField(max_length=250, blank=True)
	type_contact = models.CharField(max_length=250, blank=True, choices=CONTACT_TYPE_CHOICES)
	contacts = models.ManyToManyField('self', through='ContactRelationship', symmetrical=False, related_name='related_contacts+')

	def __unicode__(self):
		return self.firstname + ' ' + self.lastname

	def __str__(self):
		return self.firstname + ' ' + self.lastname


class ContactMoreInfo(models.Model):
	contact = models.ForeignKey(Contact, related_name='contact_moreinfo')
	info = models.CharField(max_length=240)
	type_info = models.CharField(max_length=240, choices=MOREINFO_CHOICES)

	def __unicode__(self):
		return self.contact + ' - ' + self.type_info + ' : ' + self.info

	def __str__(self):
		return self.contact + ' - ' + self.type_info + ' : ' + self.info


class ContactRelationship(models.Model):
	relation = models.CharField(max_length=200, blank=True)
	from_contact = models.ForeignKey('Contact', related_name='from_contacts')
	to_contact = models.ForeignKey('Contact', related_name='to_contacts')

	class Meta:
		unique_together = ('from_contact', 'to_contact')