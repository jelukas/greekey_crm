# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Milestone'
        db.create_table(u'projects_milestone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='milestones', to=orm['projects.Project'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('completed_prevission', self.gf('django.db.models.fields.DateTimeField')()),
            ('completed_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Milestone'])

        # Adding model 'TaskTimer'
        db.create_table(u'projects_tasktimer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('stop_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tasks_timers', to=orm['auth.User'])),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(related_name='timers', to=orm['projects.Task'])),
        ))
        db.send_create_signal(u'projects', ['TaskTimer'])

        # Adding model 'Project'
        db.create_table(u'projects_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects', to=orm['contacts.Company'])),
        ))
        db.send_create_signal(u'projects', ['Project'])

        # Adding M2M table for field members on 'Project'
        m2m_table_name = db.shorten_name(u'projects_project_members')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'user_id'])

        # Adding model 'Task'
        db.create_table(u'projects_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('milestone', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tasks', to=orm['projects.Milestone'])),
            ('asiggned_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tasks', to=orm['auth.User'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('duration', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'projects', ['Task'])


    def backwards(self, orm):
        # Deleting model 'Milestone'
        db.delete_table(u'projects_milestone')

        # Deleting model 'TaskTimer'
        db.delete_table(u'projects_tasktimer')

        # Deleting model 'Project'
        db.delete_table(u'projects_project')

        # Removing M2M table for field members on 'Project'
        db.delete_table(db.shorten_name(u'projects_project_members'))

        # Deleting model 'Task'
        db.delete_table(u'projects_task')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'projects.milestone': {
            'Meta': {'object_name': 'Milestone'},
            'completed_prevission': ('django.db.models.fields.DateTimeField', [], {}),
            'completed_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'milestones'", 'to': u"orm['projects.Project']"})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects'", 'to': u"orm['contacts.Company']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'projects.task': {
            'Meta': {'object_name': 'Task'},
            'asiggned_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tasks'", 'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tasks'", 'to': u"orm['projects.Milestone']"})
        },
        u'projects.tasktimer': {
            'Meta': {'object_name': 'TaskTimer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'stop_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'timers'", 'to': u"orm['projects.Task']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tasks_timers'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['projects']