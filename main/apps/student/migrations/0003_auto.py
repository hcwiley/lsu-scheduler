# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding M2M table for field coursesRequired on 'Major'
        db.create_table('student_major_coursesRequired', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('major', models.ForeignKey(orm['student.major'], null=False)),
            ('course', models.ForeignKey(orm['course.course'], null=False))
        ))
        db.create_unique('student_major_coursesRequired', ['major_id', 'course_id'])

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
        
        # Removing M2M table for field coursesRequired on 'Major'
        db.delete_table('student_major_coursesRequired')

        # Removing M2M table for field coursesWanted on 'Student'
        db.delete_table('student_student_coursesWanted')

        # Removing M2M table for field coursesRegistered on 'Student'
        db.delete_table('student_student_coursesRegistered')

        # Removing M2M table for field coursesNeeded on 'Student'
        db.delete_table('student_student_coursesNeeded')


    models = {
        'course.course': {
            'Meta': {'object_name': 'Course'},
            'abbr': ('django.db.models.fields.CharField', [], {'default': "'FOO'", 'max_length': '4'}),
            'available_seats': ('django.db.models.fields.IntegerField', [], {'default': '42', 'null': 'True', 'blank': 'True'}),
            'building': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'credit_hours': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'days': ('django.db.models.fields.related.ManyToManyField', [], {'default': "''", 'to': "orm['course.Date']", 'symmetrical': 'False'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(17, 2, 45, 159000)', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructor': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'number_enrolled': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'room': ('django.db.models.fields.IntegerField', [], {'default': '42', 'null': 'True', 'blank': 'True'}),
            'section_number': ('django.db.models.fields.IntegerField', [], {}),
            'special_enrollment': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(17, 2, 45, 159000)', 'null': 'True', 'blank': 'True'}),
            'time_tba': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '3', 'null': 'True', 'blank': 'True'})
        },
        'course.date': {
            'Meta': {'object_name': 'Date'},
            'day': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'student.major': {
            'Meta': {'object_name': 'Major'},
            'college': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'coursesRequired': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Required_Course'", 'symmetrical': 'False', 'to': "orm['course.Course']"}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'student.minor': {
            'Meta': {'object_name': 'Minor', '_ormbases': ['student.Major']},
            'major_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['student.Major']", 'unique': 'True', 'primary_key': 'True'})
        },
        'student.student': {
            'Meta': {'object_name': 'Student'},
            'coursesNeeded': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Needed_Course'", 'symmetrical': 'False', 'to': "orm['course.Course']"}),
            'coursesRegistered': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Registered_Course'", 'symmetrical': 'False', 'to': "orm['course.Course']"}),
            'coursesWanted': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Wanted_Course'", 'symmetrical': 'False', 'to': "orm['course.Course']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'major': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['student.Major']"}),
            'minor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Minor'", 'to': "orm['student.Minor']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '144'})
        }
    }

    complete_apps = ['student']
