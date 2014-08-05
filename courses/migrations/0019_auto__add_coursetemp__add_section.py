# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CourseTemp'
        db.create_table(u'courses_coursetemp', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dept', self.gf('django.db.models.fields.CharField')(default='None assigned', max_length=200)),
            ('code', self.gf('django.db.models.fields.CharField')(default='None assigned', max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(default='None assigned', max_length=200)),
            ('credit_hours', self.gf('django.db.models.fields.CharField')(default='None assigned', max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(default='None assigned', max_length=200)),
            ('addit_info', self.gf('django.db.models.fields.CharField')(default='None assigned', max_length=200)),
            ('by_permission', self.gf('django.db.models.fields.CharField')(default='None assigned', max_length=200)),
            ('prereq', self.gf('django.db.models.fields.CharField')(default='None assigned', max_length=200)),
            ('notes', self.gf('django.db.models.fields.CharField')(default='None assigned', max_length=200)),
            ('xlisted', self.gf('django.db.models.fields.CharField')(default='None assigned', max_length=200)),
            ('ratings', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Rating'])),
        ))
        db.send_create_signal(u'courses', ['CourseTemp'])

        # Adding M2M table for field dists on 'CourseTemp'
        m2m_table_name = db.shorten_name(u'courses_coursetemp_dists')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coursetemp', models.ForeignKey(orm[u'courses.coursetemp'], null=False)),
            ('distribution', models.ForeignKey(orm[u'courses.distribution'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coursetemp_id', 'distribution_id'])

        # Adding M2M table for field sections on 'CourseTemp'
        m2m_table_name = db.shorten_name(u'courses_coursetemp_sections')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coursetemp', models.ForeignKey(orm[u'courses.coursetemp'], null=False)),
            ('section', models.ForeignKey(orm[u'courses.section'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coursetemp_id', 'section_id'])

        # Adding model 'Section'
        db.create_table(u'courses_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section_id', self.gf('django.db.models.fields.CharField')(default='None assigned', max_length=200)),
            ('crn', self.gf('django.db.models.fields.CharField')(default='None assigned', max_length=200)),
            ('seats_available', self.gf('django.db.models.fields.CharField')(default='None assigned', max_length=200)),
            ('max_enrollment', self.gf('django.db.models.fields.CharField')(default='None assigned', max_length=200)),
            ('prof', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Professor'])),
            ('timeanddate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.TimeAndDate'])),
            ('semester', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Semester'])),
        ))
        db.send_create_signal(u'courses', ['Section'])


    def backwards(self, orm):
        # Deleting model 'CourseTemp'
        db.delete_table(u'courses_coursetemp')

        # Removing M2M table for field dists on 'CourseTemp'
        db.delete_table(db.shorten_name(u'courses_coursetemp_dists'))

        # Removing M2M table for field sections on 'CourseTemp'
        db.delete_table(db.shorten_name(u'courses_coursetemp_sections'))

        # Deleting model 'Section'
        db.delete_table(u'courses_section')


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
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'courses.course': {
            'Meta': {'ordering': "['code']", 'object_name': 'Course'},
            'addit_info': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'by_permission': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'code': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'credit_hours': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'crn': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'date': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'dept': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'dists': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courses.Distribution']", 'symmetrical': 'False'}),
            'endtime': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_enrollment': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'notes': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'prereq': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'prof': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'professor': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courses.Professor']", 'symmetrical': 'False'}),
            'rating': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courses.Rating']", 'symmetrical': 'False'}),
            'seats_available': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'semester': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courses.Semester']", 'symmetrical': 'False'}),
            'starttime': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'timeanddate': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courses.TimeAndDate']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'xlisted': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'})
        },
        u'courses.coursebucket': {
            'Meta': {'object_name': 'CourseBucket'},
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courses.Course']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Major']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'num_pick': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'courses.coursetemp': {
            'Meta': {'object_name': 'CourseTemp'},
            'addit_info': ('django.db.models.fields.CharField', [], {'default': "'None assigned'", 'max_length': '200'}),
            'by_permission': ('django.db.models.fields.CharField', [], {'default': "'None assigned'", 'max_length': '200'}),
            'code': ('django.db.models.fields.CharField', [], {'default': "'None assigned'", 'max_length': '200'}),
            'credit_hours': ('django.db.models.fields.CharField', [], {'default': "'None assigned'", 'max_length': '200'}),
            'dept': ('django.db.models.fields.CharField', [], {'default': "'None assigned'", 'max_length': '200'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "'None assigned'", 'max_length': '200'}),
            'dists': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courses.Distribution']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'default': "'None assigned'", 'max_length': '200'}),
            'prereq': ('django.db.models.fields.CharField', [], {'default': "'None assigned'", 'max_length': '200'}),
            'ratings': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Rating']"}),
            'sections': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courses.Section']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'None assigned'", 'max_length': '200'}),
            'xlisted': ('django.db.models.fields.CharField', [], {'default': "'None assigned'", 'max_length': '200'})
        },
        u'courses.distribution': {
            'Meta': {'ordering': "['name']", 'object_name': 'Distribution'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '200'})
        },
        u'courses.major': {
            'Meta': {'ordering': "['name']", 'object_name': 'Major'},
            'code': ('django.db.models.fields.CharField', [], {'default': "'UND'", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_minor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Undecided'", 'max_length': '200'})
        },
        u'courses.professor': {
            'Meta': {'ordering': "['name']", 'object_name': 'Professor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'rating': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Rating']"}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'courses.rating': {
            'Meta': {'object_name': 'Rating'},
            'comment_author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Student']"}),
            'comment_text': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '5'})
        },
        u'courses.section': {
            'Meta': {'object_name': 'Section'},
            'crn': ('django.db.models.fields.CharField', [], {'default': "'None assigned'", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_enrollment': ('django.db.models.fields.CharField', [], {'default': "'None assigned'", 'max_length': '200'}),
            'prof': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Professor']"}),
            'seats_available': ('django.db.models.fields.CharField', [], {'default': "'None assigned'", 'max_length': '200'}),
            'section_id': ('django.db.models.fields.CharField', [], {'default': "'None assigned'", 'max_length': '200'}),
            'semester': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Semester']"}),
            'timeanddate': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.TimeAndDate']"})
        },
        u'courses.semester': {
            'Meta': {'ordering': "['year']", 'object_name': 'Semester'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'session': ('django.db.models.fields.CharField', [], {'default': "'Fall'", 'max_length': '200'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'courses.student': {
            'Meta': {'unique_together': "(('primary_major', 'secondary_major'),)", 'object_name': 'Student'},
            'class_year': ('django.db.models.fields.CharField', [], {'default': "'fy'", 'max_length': '200'}),
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['courses.Course']", 'null': 'True', 'blank': 'True'}),
            'foreign_lang_passed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gpa': ('django.db.models.fields.FloatField', [], {'default': '2.0', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'primary_major': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'primary major'", 'null': 'True', 'to': u"orm['courses.Major']"}),
            'qrb_passed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'secondary_major': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'secondary major'", 'null': 'True', 'to': u"orm['courses.Major']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'courses.timeanddate': {
            'Meta': {'object_name': 'TimeAndDate'},
            'dates': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'endtime': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'starttime': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'courses.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'email_verified': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['courses']