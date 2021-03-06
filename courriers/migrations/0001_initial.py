# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NewsletterList'
        db.create_table(u'courriers_newsletterlist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('languages', self.gf('separatedvaluesfield.models.SeparatedValuesField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'courriers', ['NewsletterList'])

        # Adding model 'Newsletter'
        db.create_table(u'courriers_newsletter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('published_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('status', self.gf('django.db.models.fields.PositiveIntegerField')(default=2, max_length=1, db_index=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('languages', self.gf('separatedvaluesfield.models.SeparatedValuesField')(max_length=50, null=True, blank=True)),
            ('newsletter_list', self.gf('django.db.models.fields.related.ForeignKey')(related_name='newsletters', to=orm['courriers.NewsletterList'])),
            ('sent', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
        ))
        db.send_create_signal(u'courriers', ['Newsletter'])

        # Adding model 'NewsletterItem'
        db.create_table(u'courriers_newsletteritem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('newsletter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='items', to=orm['courriers.Newsletter'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'courriers', ['NewsletterItem'])

        # Adding model 'NewsletterSubscriber'
        db.create_table(u'courriers_newslettersubscriber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subscribed_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('is_unsubscribed', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=250)),
            ('lang', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('newsletter_list', self.gf('django.db.models.fields.related.ForeignKey')(related_name='newsletter_subscribers', to=orm['courriers.NewsletterList'])),
        ))
        db.send_create_signal(u'courriers', ['NewsletterSubscriber'])


    def backwards(self, orm):
        # Deleting model 'NewsletterList'
        db.delete_table(u'courriers_newsletterlist')

        # Deleting model 'Newsletter'
        db.delete_table(u'courriers_newsletter')

        # Deleting model 'NewsletterItem'
        db.delete_table(u'courriers_newsletteritem')

        # Deleting model 'NewsletterSubscriber'
        db.delete_table(u'courriers_newslettersubscriber')


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
            'username': ('sluggable.fields.SluggableField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'courriers.newsletter': {
            'Meta': {'object_name': 'Newsletter'},
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'languages': ('separatedvaluesfield.models.SeparatedValuesField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'newsletter_list': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'newsletters'", 'to': u"orm['courriers.NewsletterList']"}),
            'published_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2', 'max_length': '1', 'db_index': 'True'})
        },
        u'courriers.newsletteritem': {
            'Meta': {'object_name': 'NewsletterItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'newsletter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['courriers.Newsletter']"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'courriers.newsletterlist': {
            'Meta': {'object_name': 'NewsletterList'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'languages': ('separatedvaluesfield.models.SeparatedValuesField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'courriers.newslettersubscriber': {
            'Meta': {'object_name': 'NewsletterSubscriber'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_unsubscribed': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'newsletter_list': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'newsletter_subscribers'", 'to': u"orm['courriers.NewsletterList']"}),
            'subscribed_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        }
    }

    complete_apps = ['courriers']