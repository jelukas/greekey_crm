# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EmailAddresses'
        db.create_table(u'contacts_emailaddresses', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email_address', self.gf('django.db.models.fields.CharField')(max_length=230)),
        ))
        db.send_create_signal(u'contacts', ['EmailAddresses'])

        # Adding model 'Company'
        db.create_table(u'contacts_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('primary_address', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('primary_phone', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
        ))
        db.send_create_signal(u'contacts', ['Company'])

        # Adding model 'PhoneNumbers'
        db.create_table(u'contacts_phonenumbers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=230)),
        ))
        db.send_create_signal(u'contacts', ['PhoneNumbers'])

        # Adding model 'Contact'
        db.create_table(u'contacts_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('primary_email', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('primary_address', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('primary_phone', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
        ))
        db.send_create_signal(u'contacts', ['Contact'])

        # Adding model 'CompanyContacts'
        db.create_table(u'contacts_companycontacts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Company'])),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Contact'])),
            ('job_position', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'contacts', ['CompanyContacts'])


    def backwards(self, orm):
        # Deleting model 'EmailAddresses'
        db.delete_table(u'contacts_emailaddresses')

        # Deleting model 'Company'
        db.delete_table(u'contacts_company')

        # Deleting model 'PhoneNumbers'
        db.delete_table(u'contacts_phonenumbers')

        # Deleting model 'Contact'
        db.delete_table(u'contacts_contact')

        # Deleting model 'CompanyContacts'
        db.delete_table(u'contacts_companycontacts')


    models = {
        u'contacts.company': {
            'Meta': {'object_name': 'Company'},
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['contacts.Contact']", 'through': u"orm['contacts.CompanyContacts']", 'symmetrical': 'False'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'primary_address': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'primary_phone': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        },
        u'contacts.companycontacts': {
            'Meta': {'object_name': 'CompanyContacts'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Company']"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_position': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'primary_address': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'primary_email': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'primary_phone': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        },
        u'contacts.emailaddresses': {
            'Meta': {'object_name': 'EmailAddresses'},
            'email_address': ('django.db.models.fields.CharField', [], {'max_length': '230'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contacts.phonenumbers': {
            'Meta': {'object_name': 'PhoneNumbers'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '230'})
        }
    }

    complete_apps = ['contacts']