# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Lab'
        db.create_table('course_lab', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('building', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True)),
            ('room', self.gf('django.db.models.fields.IntegerField')(default=42, null=True, blank=True)),
            ('instructor', self.gf('django.db.models.fields.CharField')(default='', max_length=100, null=True, blank=True)),
            ('start_time', self.gf('django.db.models.fields.TimeField')(default=datetime.time(18, 20, 2, 267693), null=True, blank=True)),
            ('end_time', self.gf('django.db.models.fields.TimeField')(default=datetime.time(18, 20, 2, 267735), null=True, blank=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['course.Course'])),
        ))
        db.send_create_signal('course', ['Lab'])

        # Adding M2M table for field days on 'Lab'
        db.create_table('course_lab_days', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lab', models.ForeignKey(orm['course.lab'], null=False)),
            ('date', models.ForeignKey(orm['course.date'], null=False))
        ))
        db.create_unique('course_lab_days', ['lab_id', 'date_id'])

        # Adding field 'Course.credit_hours'
        db.add_column('course_course', 'credit_hours', self.gf('django.db.models.fields.IntegerField')(default=3), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Lab'
        db.delete_table('course_lab')

        # Removing M2M table for field days on 'Lab'
        db.delete_table('course_lab_days')

        # Deleting field 'Course.credit_hours'
        db.delete_column('course_course', 'credit_hours')


    models = {
        'course.course': {
            'Meta': {'object_name': 'Course'},
            'abbr': ('django.db.models.fields.CharField', [], {'default': "'FOO'", 'max_length': '4'}),
            'available_seats': ('django.db.models.fields.IntegerField', [], {'default': '42', 'null': 'True', 'blank': 'True'}),
            'building': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'credit_hours': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'days': ('django.db.models.fields.related.ManyToManyField', [], {'default': "''", 'to': "orm['course.Date']", 'symmetrical': 'False'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(18, 20, 2, 265577)', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'number_enrolled': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'room': ('django.db.models.fields.IntegerField', [], {'default': '42', 'null': 'True', 'blank': 'True'}),
            'section_number': ('django.db.models.fields.IntegerField', [], {}),
            'special_enrollment': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(18, 20, 2, 265527)', 'null': 'True', 'blank': 'True'}),
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
            'end_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(18, 20, 2, 267735)', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'room': ('django.db.models.fields.IntegerField', [], {'default': '42', 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(18, 20, 2, 267693)', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['course']
