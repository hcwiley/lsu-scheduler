# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'College'
        db.create_table('college_college', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=50, null=True, db_index=True, blank=True)),
        ))
        db.send_create_signal('college', ['College'])

        # Adding model 'Department'
        db.create_table('college_department', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('abbr', self.gf('django.db.models.fields.CharField')(default='', max_length=4, unique=True, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=50, null=True, db_index=True, blank=True)),
            ('college', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['college.College'], null=True, blank=True)),
        ))
        db.send_create_signal('college', ['Department'])

        # Adding model 'Major'
        db.create_table('college_major', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['college.Department'], null=True, blank=True)),
        ))
        db.send_create_signal('college', ['Major'])

        # Adding M2M table for field coursesRequired on 'Major'
        db.create_table('college_major_coursesRequired', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('major', models.ForeignKey(orm['college.major'], null=False)),
            ('course', models.ForeignKey(orm['course.course'], null=False))
        ))
        db.create_unique('college_major_coursesRequired', ['major_id', 'course_id'])

        # Adding model 'Minor'
        db.create_table('college_minor', (
            ('major_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['college.Major'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('college', ['Minor'])


    def backwards(self, orm):
        
        # Deleting model 'College'
        db.delete_table('college_college')

        # Deleting model 'Department'
        db.delete_table('college_department')

        # Deleting model 'Major'
        db.delete_table('college_major')

        # Removing M2M table for field coursesRequired on 'Major'
        db.delete_table('college_major_coursesRequired')

        # Deleting model 'Minor'
        db.delete_table('college_minor')


    models = {
        'college.college': {
            'Meta': {'object_name': 'College'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        'college.department': {
            'Meta': {'object_name': 'Department'},
            'abbr': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'college': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['college.College']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        'college.major': {
            'Meta': {'object_name': 'Major'},
            'coursesRequired': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Required_Course'", 'default': 'None', 'to': "orm['course.Course']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['college.Department']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'college.minor': {
            'Meta': {'object_name': 'Minor', '_ormbases': ['college.Major']},
            'major_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['college.Major']", 'unique': 'True', 'primary_key': 'True'})
        },
        'course.course': {
            'Meta': {'object_name': 'Course'},
            'available_seats': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'building': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'credit_hours': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'days': ('django.db.models.fields.related.ManyToManyField', [], {'default': "''", 'to': "orm['course.Date']", 'symmetrical': 'False'}),
            'department': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'number_enrolled': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
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
        }
    }

    complete_apps = ['college']
