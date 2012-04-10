# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Student'
        db.create_table('student_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=144)),
            ('id_number', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('major', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['college.Major'])),
            ('minor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Minor', to=orm['college.Minor'])),
        ))
        db.send_create_signal('student', ['Student'])

        # Adding M2M table for field coursesWanted on 'Student'
        db.create_table('student_student_coursesWanted', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('student', models.ForeignKey(orm['student.student'], null=False)),
            ('course', models.ForeignKey(orm['course.course'], null=False))
        ))
        db.create_unique('student_student_coursesWanted', ['student_id', 'course_id'])

        # Adding M2M table for field coursesRegistered on 'Student'
        db.create_table('student_student_coursesRegistered', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('student', models.ForeignKey(orm['student.student'], null=False)),
            ('course', models.ForeignKey(orm['course.course'], null=False))
        ))
        db.create_unique('student_student_coursesRegistered', ['student_id', 'course_id'])

        # Adding M2M table for field coursesNeeded on 'Student'
        db.create_table('student_student_coursesNeeded', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('student', models.ForeignKey(orm['student.student'], null=False)),
            ('course', models.ForeignKey(orm['course.course'], null=False))
        ))
        db.create_unique('student_student_coursesNeeded', ['student_id', 'course_id'])


    def backwards(self, orm):
        
        # Deleting model 'Student'
        db.delete_table('student_student')

        # Removing M2M table for field coursesWanted on 'Student'
        db.delete_table('student_student_coursesWanted')

        # Removing M2M table for field coursesRegistered on 'Student'
        db.delete_table('student_student_coursesRegistered')

        # Removing M2M table for field coursesNeeded on 'Student'
        db.delete_table('student_student_coursesNeeded')


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
        },
        'student.student': {
            'Meta': {'object_name': 'Student'},
            'coursesNeeded': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Needed_Course'", 'symmetrical': 'False', 'to': "orm['course.Course']"}),
            'coursesRegistered': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Registered_Course'", 'symmetrical': 'False', 'to': "orm['course.Course']"}),
            'coursesWanted': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Wanted_Course'", 'symmetrical': 'False', 'to': "orm['course.Course']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'major': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['college.Major']"}),
            'minor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Minor'", 'to': "orm['college.Minor']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '144'})
        }
    }

    complete_apps = ['student']
