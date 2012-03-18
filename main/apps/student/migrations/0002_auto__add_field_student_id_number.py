# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Student.id_number'
        db.add_column('student_student', 'id_number', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Student.id_number'
        db.delete_column('student_student', 'id_number')


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
            'id_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'major': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['student.Major']"}),
            'minor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Minor'", 'to': "orm['student.Minor']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '144'})
        }
    }

    complete_apps = ['student']
