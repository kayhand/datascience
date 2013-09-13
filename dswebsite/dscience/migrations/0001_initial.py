# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Topic'
        db.create_table(u'dscience_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'dscience', ['Topic'])

        # Adding model 'Presentation'
        db.create_table(u'dscience_presentation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dscience.Topic'])),
            ('first_due_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('upload_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('pFile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'dscience', ['Presentation'])

        # Adding model 'Group'
        db.create_table(u'dscience_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('presentation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dscience.Presentation'])),
        ))
        db.send_create_signal(u'dscience', ['Group'])

        # Adding model 'UserProfile'
        db.create_table(u'dscience_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dscience.Group'])),
        ))
        db.send_create_signal(u'dscience', ['UserProfile'])

        # Adding model 'Assignment'
        db.create_table(u'dscience_assignment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dscience.Group'])),
            ('file_path', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('upload_due_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('due_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'dscience', ['Assignment'])

        # Adding model 'Homework'
        db.create_table(u'dscience_homework', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('assignment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dscience.Assignment'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dscience.UserProfile'])),
            ('upload_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'dscience', ['Homework'])


    def backwards(self, orm):
        # Deleting model 'Topic'
        db.delete_table(u'dscience_topic')

        # Deleting model 'Presentation'
        db.delete_table(u'dscience_presentation')

        # Deleting model 'Group'
        db.delete_table(u'dscience_group')

        # Deleting model 'UserProfile'
        db.delete_table(u'dscience_userprofile')

        # Deleting model 'Assignment'
        db.delete_table(u'dscience_assignment')

        # Deleting model 'Homework'
        db.delete_table(u'dscience_homework')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dscience.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'due_date': ('django.db.models.fields.DateTimeField', [], {}),
            'file_path': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dscience.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'upload_due_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'dscience.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'presentation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dscience.Presentation']"})
        },
        u'dscience.homework': {
            'Meta': {'object_name': 'Homework'},
            'assignment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dscience.Assignment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'upload_date': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dscience.UserProfile']"})
        },
        u'dscience.presentation': {
            'Meta': {'object_name': 'Presentation'},
            'first_due_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'pFile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dscience.Topic']"}),
            'upload_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'dscience.topic': {
            'Meta': {'object_name': 'Topic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'dscience.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dscience.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['dscience']