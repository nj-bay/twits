# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'tweets_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'tweets', ['User'])

        # Adding model 'Tweet'
        db.create_table(u'tweets_tweet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('tweet', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal(u'tweets', ['Tweet'])

        # Adding model 'Comment'
        db.create_table(u'tweets_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'tweets', ['Comment'])

        # Adding model 'Likes'
        db.create_table(u'tweets_likes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('like', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'tweets', ['Likes'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'tweets_user')

        # Deleting model 'Tweet'
        db.delete_table(u'tweets_tweet')

        # Deleting model 'Comment'
        db.delete_table(u'tweets_comment')

        # Deleting model 'Likes'
        db.delete_table(u'tweets_likes')


    models = {
        u'tweets.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'tweets.likes': {
            'Meta': {'object_name': 'Likes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'like': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'tweets.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'tweet': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'tweets.user': {
            'Meta': {'object_name': 'User'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['tweets']