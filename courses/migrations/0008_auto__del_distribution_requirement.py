# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Distribution_Requirement'
        db.delete_table(u'courses_distribution_requirement')

        # Removing M2M table for field dists on 'Distribution_Requirement'
        db.delete_table(db.shorten_name(u'courses_distribution_requirement_dists'))


    def backwards(self, orm):
        # Adding model 'Distribution_Requirement'
        db.create_table(u'courses_distribution_requirement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'courses', ['Distribution_Requirement'])

        # Adding M2M table for field dists on 'Distribution_Requirement'
        m2m_table_name = db.shorten_name(u'courses_distribution_requirement_dists')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('distribution_requirement', models.ForeignKey(orm[u'courses.distribution_requirement'], null=False)),
            ('distribution', models.ForeignKey(orm[u'courses.distribution'], null=False))
        ))
        db.create_unique(m2m_table_name, ['distribution_requirement_id', 'distribution_id'])


    models = {
        u'courses.course': {
            'Meta': {'ordering': "['name']", 'object_name': 'Course'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'comments': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'dists': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courses.Distribution']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'prof': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'prof_site': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'courses.course_bucket': {
            'Meta': {'object_name': 'Course_Bucket'},
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courses.Course']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'courses.distribution': {
            'Meta': {'object_name': 'Distribution'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '5'})
        },
        u'courses.enrollment': {
            'Meta': {'object_name': 'Enrollment'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Course']"}),
            'date_taken': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Student']"})
        },
        u'courses.major': {
            'Meta': {'object_name': 'Major'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Undecided'", 'max_length': '5'})
        },
        u'courses.student': {
            'Meta': {'object_name': 'Student'},
            'class_year': ('django.db.models.fields.CharField', [], {'default': "'fy'", 'max_length': '5'}),
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courses.Course']", 'through': u"orm['courses.Enrollment']", 'symmetrical': 'False'}),
            'distribution_requirements_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'gpa': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'major_requirements_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_major': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'primary major'", 'to': u"orm['courses.Major']"}),
            'secondary_major': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'secondary major'", 'to': u"orm['courses.Major']"})
        }
    }

    complete_apps = ['courses']