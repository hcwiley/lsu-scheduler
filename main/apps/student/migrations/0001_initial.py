# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Major'
        db.create_table('student_major', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('college', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('student', ['Major'])

        # Adding model 'Minor'
        db.create_table('student_minor', (
            ('major_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['student.Major'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('student', ['Minor'])

        # Adding model 'Student'
        db.create_table('student_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=144)),
            ('major', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['student.Major'])),
            ('minor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Minor', to=orm['student.Minor'])),
        ))
        db.send_create_signal('student', ['Student'])


    def backwards(self, orm):
        
        # Deleting model 'Major'
        db.delete_table('student_major')

        # Deleting model 'Minor'
        db.delete_table('student_minor')

        # Deleting model 'Student'
        db.delete_table('student_student')


    models = {
        'student.major': {
            'Meta': {'object_name': 'Major'},
            'college': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['student.Major']"}),
            'minor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Minor'", 'to': "orm['student.Minor']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '144'})
        }
    }

    complete_apps = ['student']
