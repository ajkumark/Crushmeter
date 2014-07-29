# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Crush.time'
        db.add_column(u'crushapp_crush', 'time',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 29, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Crush.time'
        db.delete_column(u'crushapp_crush', 'time')


    models = {
        u'crushapp.crush': {
            'Meta': {'object_name': 'Crush'},
            'crush': ('django.db.models.fields.IntegerField', [], {}),
            'crush_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['crushapp']