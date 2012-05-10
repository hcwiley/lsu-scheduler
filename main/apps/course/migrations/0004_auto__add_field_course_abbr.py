# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Course.abbr'
        db.add_column('course_course', 'abbr', self.gf('django.db.models.fields.CharField')(default='', max_length=4, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Course.abbr'
        db.delete_column('course_course', 'abbr')


    models = {
        'course.course': {
            'Meta': {'ordering': "['number']", 'object_name': 'Course'},
            'abbr': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'available_seats': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'building': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'credit_hours': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'days': ('django.db.models.fields.related.ManyToManyField', [], {'default': "''", 'to': "orm['course.Date']", 'symmetrical': 'False'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'number_enrolled': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'pretty_days': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'pretty_end': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'pretty_start': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'room': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'section_number': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'special_enrollment': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'time_tba': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '3', 'null': 'True', 'blank': 'True'})
        },
        'course.date': {
            'Meta': {'object_name': 'Date'},
            'day': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'course.lab': {
            'Meta': {'object_name': 'Lab'},
            'building': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['course.Course']"}),
            'days': ('django.db.models.fields.related.ManyToManyField', [], {'default': "''", 'to': "orm['course.Date']", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(0, 18, 51, 516000)', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'room': ('django.db.models.fields.IntegerField', [], {'default': '42', 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(0, 18, 51, 516000)', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['course']
