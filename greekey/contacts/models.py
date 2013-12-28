from django.db import models


class Contact(models.Model):
	firstname = models.CharField(max_length=250)
	lastname = models.CharField(max_length=250, blank=True)
	primary_email = models.CharField(max_length=250,blank=True)
	primary_address = models.CharField(max_length=250,blank=True)
	primary_phone = models.CharField(max_length=250, blank=True)

	def __unicode__(self):
		return self.firstname + ' ' + self.lastname

	def __str__(self):
		return self.firstname + ' ' + self.lastname


#TODO Contact has Many EmailAddresses.
class EmailAddresses(models.Model):
	email_address = models.CharField(max_length=230)


#TODO Contact has Many PhoneNumbers.
class PhoneNumbers(models.Model):
	phone_number = models.CharField(max_length=230)


class Company(models.Model):
	name = models.CharField(max_length=250)
	country = models.CharField(max_length=200)
	primary_address = models.CharField(max_length=250, blank=True)
	primary_phone = models.CharField(max_length=250, blank=True)
	contacts = models.ManyToManyField(Contact, through='CompanyContacts')

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name


class CompanyContacts(models.Model):
	company = models.ForeignKey(Company)
	contact = models.ForeignKey(Contact)
	job_position = models.CharField(max_length=200, blank=True)

	def __unicode__(self):
		return self.company + ' - ' + self.contact

	def __str__(self):
		return self.company + ' - ' + self.contact