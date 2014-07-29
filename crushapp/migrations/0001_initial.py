# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Crush'
        db.create_table(u'crushapp_crush', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('crush_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('crush', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'crushapp', ['Crush'])


    def backwards(self, orm):
        # Deleting model 'Crush'
        db.delete_table(u'crushapp_crush')


    models = {
        u'crushapp.crush': {
            'Meta': {'object_name': 'Crush'},
            'crush': ('django.db.models.fields.IntegerField', [], {}),
            'crush_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['crushapp']