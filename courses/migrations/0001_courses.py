# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Distribution'
        db.create_table(u'courses_distribution', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='NONE', max_length=200)),
        ))
        db.send_create_signal(u'courses', ['Distribution'])

        # Adding model 'Professor'
        db.create_table(u'courses_professor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('site', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'courses', ['Professor'])

        # Adding model 'TimeAndDate'
        db.create_table(u'courses_timeanddate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dates', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('starttime', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('endtime', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'courses', ['TimeAndDate'])

        # Adding model 'Semester'
        db.create_table(u'courses_semester', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('session', self.gf('django.db.models.fields.CharField')(default='Fall', max_length=200)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'courses', ['Semester'])

        # Adding model 'Section'
        db.create_table(u'courses_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sec_id', self.gf('django.db.models.fields.CharField')(default='None assigned', max_length=200)),
            ('crn', self.gf('django.db.models.fields.CharField')(default='None assigned', max_length=200)),
            ('seats_available', self.gf('django.db.models.fields.CharField')(default='None assigned', max_length=200)),
            ('max_enrollment', self.gf('django.db.models.fields.CharField')(default='None assigned', max_length=200)),
            ('prof', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Professor'])),
            ('timeanddate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.TimeAndDate'])),
            ('semester', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Semester'])),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Course'])),
        ))
        db.send_create_signal(u'courses', ['Section'])

        # Adding model 'Course'
        db.create_table(u'courses_course', (
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
        ))
        db.send_create_signal(u'courses', ['Course'])

        # Adding M2M table for field dists on 'Course'
        m2m_table_name = db.shorten_name(u'courses_course_dists')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('course', models.ForeignKey(orm[u'courses.course'], null=False)),
            ('distribution', models.ForeignKey(orm[u'courses.distribution'], null=False))
        ))
        db.create_unique(m2m_table_name, ['course_id', 'distribution_id'])

        # Adding model 'Student'
        db.create_table(u'courses_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('class_year', self.gf('django.db.models.fields.CharField')(default='fy', max_length=200)),
            ('primary_major', self.gf('django.db.models.fields.related.ForeignKey')(related_name='primary major', null=True, to=orm['courses.Major'])),
            ('secondary_major', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='secondary major', null=True, to=orm['courses.Major'])),
            ('gpa', self.gf('django.db.models.fields.FloatField')(default=2.0, null=True)),
            ('qrb_passed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('foreign_lang_passed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('multi_passed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'courses', ['Student'])

        # Adding unique constraint on 'Student', fields ['primary_major', 'secondary_major']
        db.create_unique(u'courses_student', ['primary_major_id', 'secondary_major_id'])

        # Adding M2M table for field courses on 'Student'
        m2m_table_name = db.shorten_name(u'courses_student_courses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('student', models.ForeignKey(orm[u'courses.student'], null=False)),
            ('course', models.ForeignKey(orm[u'courses.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['student_id', 'course_id'])

        # Adding model 'CourseBucket'
        db.create_table(u'courses_coursebucket', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('num_pick', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('major', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Major'])),
            ('manual_completion', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'courses', ['CourseBucket'])

        # Adding M2M table for field courses on 'CourseBucket'
        m2m_table_name = db.shorten_name(u'courses_coursebucket_courses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coursebucket', models.ForeignKey(orm[u'courses.coursebucket'], null=False)),
            ('course', models.ForeignKey(orm[u'courses.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coursebucket_id', 'course_id'])

        # Adding model 'Major'
        db.create_table(u'courses_major', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(default='UND', max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Undecided', max_length=200)),
            ('is_minor', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'courses', ['Major'])

        # Adding model 'UserProfile'
        db.create_table(u'courses_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('email_verified', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'courses', ['UserProfile'])

        # Adding model 'CourseRating'
        db.create_table(u'courses_courserating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course_score', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('course_comment_text', self.gf('django.db.models.fields.CharField')(max_length=10000, null=True, blank=True)),
            ('course_comment_author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Student'])),
            ('comment_course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Course'])),
        ))
        db.send_create_signal(u'courses', ['CourseRating'])

        # Adding unique constraint on 'CourseRating', fields ['course_comment_author', 'comment_course']
        db.create_unique(u'courses_courserating', ['course_comment_author_id', 'comment_course_id'])

        # Adding model 'ProfRating'
        db.create_table(u'courses_profrating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prof_score', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('prof_comment_text', self.gf('django.db.models.fields.CharField')(max_length=10000, null=True, blank=True)),
            ('prof_comment_author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Student'])),
            ('comment_professor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Professor'])),
        ))
        db.send_create_signal(u'courses', ['ProfRating'])

        # Adding unique constraint on 'ProfRating', fields ['prof_comment_author', 'comment_professor']
        db.create_unique(u'courses_profrating', ['prof_comment_author_id', 'comment_professor_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'ProfRating', fields ['prof_comment_author', 'comment_professor']
        db.delete_unique(u'courses_profrating', ['prof_comment_author_id', 'comment_professor_id'])

        # Removing unique constraint on 'CourseRating', fields ['course_comment_author', 'comment_course']
        db.delete_unique(u'courses_courserating', ['course_comment_author_id', 'comment_course_id'])

        # Removing unique constraint on 'Student', fields ['primary_major', 'secondary_major']
        db.delete_unique(u'courses_student', ['primary_major_id', 'secondary_major_id'])

        # Deleting model 'Distribution'
        db.delete_table(u'courses_distribution')

        # Deleting model 'Professor'
        db.delete_table(u'courses_professor')

        # Deleting model 'TimeAndDate'
        db.delete_table(u'courses_timeanddate')

        # Deleting model 'Semester'
        db.delete_table(u'courses_semester')

        # Deleting model 'Section'
        db.delete_table(u'courses_section')

        # Deleting model 'Course'
        db.delete_table(u'courses_course')

        # Removing M2M table for field dists on 'Course'
        db.delete_table(db.shorten_name(u'courses_course_dists'))

        # Deleting model 'Student'
        db.delete_table(u'courses_student')

        # Removing M2M table for field courses on 'Student'
        db.delete_table(db.shorten_name(u'courses_student_courses'))

        # Deleting model 'CourseBucket'
        db.delete_table(u'courses_coursebucket')

        # Removing M2M table for field courses on 'CourseBucket'
        db.delete_table(db.shorten_name(u'courses_coursebucket_courses'))

        # Deleting model 'Major'
        db.delete_table(u'courses_major')

        # Deleting model 'UserProfile'
        db.delete_table(u'courses_userprofile')

        # Deleting model 'CourseRating'
        db.delete_table(u'courses_courserating')

        # Deleting model 'ProfRating'
        db.delete_table(u'courses_profrating')


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
            'title': ('django.db.models.fields.CharField', [], {'default': "'None assigned'", 'max_length': '200'}),
            'xlisted': ('django.db.models.fields.CharField', [], {'default': "'None assigned'", 'max_length': '200'})
        },
        u'courses.coursebucket': {
            'Meta': {'object_name': 'CourseBucket'},
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courses.Course']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Major']"}),
            'manual_completion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'num_pick': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'courses.courserating': {
            'Meta': {'unique_together': "(('course_comment_author', 'comment_course'),)", 'object_name': 'CourseRating'},
            'comment_course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Course']"}),
            'course_comment_author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Student']"}),
            'course_comment_text': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'course_score': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
            'site': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'courses.profrating': {
            'Meta': {'unique_together': "(('prof_comment_author', 'comment_professor'),)", 'object_name': 'ProfRating'},
            'comment_professor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Professor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prof_comment_author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Student']"}),
            'prof_comment_text': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'prof_score': ('django.db.models.fields.IntegerField', [], {'default': '5'})
        },
        u'courses.section': {
            'Meta': {'object_name': 'Section'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Course']"}),
            'crn': ('django.db.models.fields.CharField', [], {'default': "'None assigned'", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_enrollment': ('django.db.models.fields.CharField', [], {'default': "'None assigned'", 'max_length': '200'}),
            'prof': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Professor']"}),
            'seats_available': ('django.db.models.fields.CharField', [], {'default': "'None assigned'", 'max_length': '200'}),
            'sec_id': ('django.db.models.fields.CharField', [], {'default': "'None assigned'", 'max_length': '200'}),
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
            'multi_passed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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