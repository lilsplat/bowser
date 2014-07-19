# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'courses_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('email_verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'courses', ['UserProfile'])

        # Deleting field 'Student.last_name'
        db.delete_column(u'courses_student', 'last_name')

        # Deleting field 'Student.first_name'
        db.delete_column(u'courses_student', 'first_name')

        # Deleting field 'Student.email'
        db.delete_column(u'courses_student', 'email')

        # Adding field 'Student.user'
        db.add_column(u'courses_student', 'user',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=-10, to=orm['auth.User'], unique=True),
                      keep_default=False)


        # Changing field 'Student.gpa'
        db.alter_column(u'courses_student', 'gpa', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'courses_userprofile')


        # User chose to not deal with backwards NULL issues for 'Student.last_name'
        raise RuntimeError("Cannot reverse this migration. 'Student.last_name' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Student.first_name'
        raise RuntimeError("Cannot reverse this migration. 'Student.first_name' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Student.email'
        raise RuntimeError("Cannot reverse this migration. 'Student.email' and its values cannot be restored.")
        # Deleting field 'Student.user'
        db.delete_column(u'courses_student', 'user_id')


        # Changing field 'Student.gpa'
        db.alter_column(u'courses_student', 'gpa', self.gf('django.db.models.fields.IntegerField')(default=-4.0))

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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
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
            'Meta': {'ordering': "['name']", 'object_name': 'Course'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'dept': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
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
            'name': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '200'})
        },
        u'courses.enrollment': {
            'Meta': {'unique_together': "[('student', 'course')]", 'object_name': 'Enrollment'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Course']"}),
            'date_taken': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Student']"})
        },
        u'courses.major': {
            'Meta': {'object_name': 'Major'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Undecided'", 'max_length': '200'})
        },
        u'courses.student': {
            'Meta': {'object_name': 'Student'},
            'class_year': ('django.db.models.fields.CharField', [], {'default': "'fy'", 'max_length': '200'}),
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courses.Course']", 'null': 'True', 'through': u"orm['courses.Enrollment']", 'symmetrical': 'False'}),
            'distribution_requirements_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'foreign_lang_passed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gpa': ('django.db.models.fields.FloatField', [], {'default': '2.0', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major_requirements_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_major': ('django.db.models.fields.related.ForeignKey', [], {'default': "'Undecided'", 'related_name': "'primary major'", 'to': u"orm['courses.Major']"}),
            'qrb_passed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'secondary_major': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'secondary major'", 'null': 'True', 'to': u"orm['courses.Major']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'courses.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'email_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['courses']