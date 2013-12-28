from django.contrib import admin
from .models import Contact, Company, CompanyContacts, PhoneNumbers, EmailAddresses


admin.site.register(Contact)
admin.site.register(Company)
admin.site.register(CompanyContacts)
admin.site.register(PhoneNumbers)
admin.site.register(EmailAddresses)