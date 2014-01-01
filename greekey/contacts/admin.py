from django.contrib import admin
from .models import Contact, ContactMoreInfo, ContactRelationship


admin.site.register(Contact)
admin.site.register(ContactMoreInfo)
admin.site.register(ContactRelationship)
