# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table(u'truenorth_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['login.MyUser'], unique=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=7, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('landline', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('centre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.Centre'])),
            ('address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('office_number', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('grade', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('guardian_1', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='guardian_1', null=True, to=orm['truenorth.Guardian'])),
            ('guardian_2', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='guardian_2', null=True, to=orm['truenorth.Guardian'])),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'truenorth', ['Student'])

        # Adding model 'Tutor'
        db.create_table(u'truenorth_tutor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['login.MyUser'], unique=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('pan_number', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cell_number', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('landline', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('office_number', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
        ))
        db.send_create_signal(u'truenorth', ['Tutor'])

        # Adding model 'Staff'
        db.create_table(u'truenorth_staff', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['login.MyUser'], unique=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('pan_number', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cell_number', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('landline', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'truenorth', ['Staff'])

        # Adding model 'Guardian'
        db.create_table(u'truenorth_guardian', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['login.MyUser'], unique=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'truenorth', ['Guardian'])

        # Adding model 'Centre'
        db.create_table(u'truenorth_centre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('address', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'truenorth', ['Centre'])

        # Adding model 'Course'
        db.create_table(u'truenorth_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('total_score', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'truenorth', ['Course'])

        # Adding model 'CourseModule'
        db.create_table(u'truenorth_coursemodule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.Course'])),
        ))
        db.send_create_signal(u'truenorth', ['CourseModule'])

        # Adding model 'CourseSection'
        db.create_table(u'truenorth_coursesection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.Course'])),
            ('total_marks', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'truenorth', ['CourseSection'])

        # Adding model 'Worksheet'
        db.create_table(u'truenorth_worksheet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('module', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.CourseModule'])),
        ))
        db.send_create_signal(u'truenorth', ['Worksheet'])

        # Adding model 'StudentWorksheet'
        db.create_table(u'truenorth_studentworksheet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.Student'])),
            ('worksheet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.Worksheet'])),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'truenorth', ['StudentWorksheet'])

        # Adding model 'FullLengthTest'
        db.create_table(u'truenorth_fulllengthtest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.Course'])),
        ))
        db.send_create_signal(u'truenorth', ['FullLengthTest'])

        # Adding model 'SectionalTest'
        db.create_table(u'truenorth_sectionaltest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.CourseSection'])),
        ))
        db.send_create_signal(u'truenorth', ['SectionalTest'])

        # Adding model 'StudentFullLengthTest'
        db.create_table(u'truenorth_studentfulllengthtest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.Student'])),
            ('test', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.FullLengthTest'])),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'truenorth', ['StudentFullLengthTest'])

        # Adding model 'StudentTestSectionalScore'
        db.create_table(u'truenorth_studenttestsectionalscore', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student_flt', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.StudentFullLengthTest'])),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.CourseSection'])),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'truenorth', ['StudentTestSectionalScore'])

        # Adding model 'StudentSectionalTest'
        db.create_table(u'truenorth_studentsectionaltest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.Student'])),
            ('sectional_test', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.SectionalTest'])),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'truenorth', ['StudentSectionalTest'])

        # Adding model 'Exam'
        db.create_table(u'truenorth_exam', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.Course'])),
        ))
        db.send_create_signal(u'truenorth', ['Exam'])

        # Adding model 'StudentExam'
        db.create_table(u'truenorth_studentexam', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.Student'])),
            ('exam', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.Exam'])),
            ('total_score', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('skipped', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('taken', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'truenorth', ['StudentExam'])

        # Adding model 'StudentExamSectionScore'
        db.create_table(u'truenorth_studentexamsectionscore', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student_exam', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.StudentExam'])),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.CourseSection'])),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'truenorth', ['StudentExamSectionScore'])

        # Adding model 'StudentCourse'
        db.create_table(u'truenorth_studentcourse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.Student'])),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.Course'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal(u'truenorth', ['StudentCourse'])

        # Adding model 'Batch'
        db.create_table(u'truenorth_batch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('centre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.Centre'])),
            ('module', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.CourseModule'])),
            ('day', self.gf('django.db.models.fields.IntegerField')()),
            ('time', self.gf('django.db.models.fields.TimeField')()),
            ('tutor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.Tutor'])),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'truenorth', ['Batch'])

        # Adding model 'Attendance'
        db.create_table(u'truenorth_attendance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('batch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.Batch'])),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('tutor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.Tutor'])),
        ))
        db.send_create_signal(u'truenorth', ['Attendance'])

        # Adding M2M table for field students on 'Attendance'
        db.create_table(u'truenorth_attendance_students', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('attendance', models.ForeignKey(orm[u'truenorth.attendance'], null=False)),
            ('student', models.ForeignKey(orm[u'truenorth.student'], null=False))
        ))
        db.create_unique(u'truenorth_attendance_students', ['attendance_id', 'student_id'])

        # Adding model 'Checkin'
        db.create_table(u'truenorth_checkin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('centre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.Centre'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['login.MyUser'])),
            ('time_in', self.gf('django.db.models.fields.DateTimeField')()),
            ('time_out', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('marked_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='marked_checkins', to=orm['login.MyUser'])),
        ))
        db.send_create_signal(u'truenorth', ['Checkin'])

        # Adding model 'Interaction'
        db.create_table(u'truenorth_interaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tutor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.Tutor'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['truenorth.Student'])),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'truenorth', ['Interaction'])


    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table(u'truenorth_student')

        # Deleting model 'Tutor'
        db.delete_table(u'truenorth_tutor')

        # Deleting model 'Staff'
        db.delete_table(u'truenorth_staff')

        # Deleting model 'Guardian'
        db.delete_table(u'truenorth_guardian')

        # Deleting model 'Centre'
        db.delete_table(u'truenorth_centre')

        # Deleting model 'Course'
        db.delete_table(u'truenorth_course')

        # Deleting model 'CourseModule'
        db.delete_table(u'truenorth_coursemodule')

        # Deleting model 'CourseSection'
        db.delete_table(u'truenorth_coursesection')

        # Deleting model 'Worksheet'
        db.delete_table(u'truenorth_worksheet')

        # Deleting model 'StudentWorksheet'
        db.delete_table(u'truenorth_studentworksheet')

        # Deleting model 'FullLengthTest'
        db.delete_table(u'truenorth_fulllengthtest')

        # Deleting model 'SectionalTest'
        db.delete_table(u'truenorth_sectionaltest')

        # Deleting model 'StudentFullLengthTest'
        db.delete_table(u'truenorth_studentfulllengthtest')

        # Deleting model 'StudentTestSectionalScore'
        db.delete_table(u'truenorth_studenttestsectionalscore')

        # Deleting model 'StudentSectionalTest'
        db.delete_table(u'truenorth_studentsectionaltest')

        # Deleting model 'Exam'
        db.delete_table(u'truenorth_exam')

        # Deleting model 'StudentExam'
        db.delete_table(u'truenorth_studentexam')

        # Deleting model 'StudentExamSectionScore'
        db.delete_table(u'truenorth_studentexamsectionscore')

        # Deleting model 'StudentCourse'
        db.delete_table(u'truenorth_studentcourse')

        # Deleting model 'Batch'
        db.delete_table(u'truenorth_batch')

        # Deleting model 'Attendance'
        db.delete_table(u'truenorth_attendance')

        # Removing M2M table for field students on 'Attendance'
        db.delete_table('truenorth_attendance_students')

        # Deleting model 'Checkin'
        db.delete_table(u'truenorth_checkin')

        # Deleting model 'Interaction'
        db.delete_table(u'truenorth_interaction')


    models = {
        u'login.myuser': {
            'Meta': {'object_name': 'MyUser'},
            'changed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'truenorth.attendance': {
            'Meta': {'object_name': 'Attendance'},
            'batch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.Batch']"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['truenorth.Student']", 'symmetrical': 'False'}),
            'tutor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.Tutor']"})
        },
        u'truenorth.batch': {
            'Meta': {'object_name': 'Batch'},
            'centre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.Centre']"}),
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'day': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.CourseModule']"}),
            'time': ('django.db.models.fields.TimeField', [], {}),
            'tutor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.Tutor']"})
        },
        u'truenorth.centre': {
            'Meta': {'object_name': 'Centre'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'truenorth.checkin': {
            'Meta': {'object_name': 'Checkin'},
            'centre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.Centre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marked_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'marked_checkins'", 'to': u"orm['login.MyUser']"}),
            'time_in': ('django.db.models.fields.DateTimeField', [], {}),
            'time_out': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['login.MyUser']"})
        },
        u'truenorth.course': {
            'Meta': {'object_name': 'Course'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'total_score': ('django.db.models.fields.IntegerField', [], {})
        },
        u'truenorth.coursemodule': {
            'Meta': {'object_name': 'CourseModule'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'truenorth.coursesection': {
            'Meta': {'object_name': 'CourseSection'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'total_marks': ('django.db.models.fields.IntegerField', [], {})
        },
        u'truenorth.exam': {
            'Meta': {'object_name': 'Exam'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.Course']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'truenorth.fulllengthtest': {
            'Meta': {'object_name': 'FullLengthTest'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.Course']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'truenorth.guardian': {
            'Meta': {'object_name': 'Guardian'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['login.MyUser']", 'unique': 'True'})
        },
        u'truenorth.interaction': {
            'Meta': {'object_name': 'Interaction'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.Student']"}),
            'tutor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.Tutor']"})
        },
        u'truenorth.sectionaltest': {
            'Meta': {'object_name': 'SectionalTest'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.CourseSection']"})
        },
        u'truenorth.staff': {
            'Meta': {'object_name': 'Staff'},
            'cell_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'landline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'pan_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['login.MyUser']", 'unique': 'True'})
        },
        u'truenorth.student': {
            'Meta': {'object_name': 'Student'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'centre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.Centre']"}),
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['truenorth.Course']", 'through': u"orm['truenorth.StudentCourse']", 'symmetrical': 'False'}),
            'exams': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['truenorth.Exam']", 'through': u"orm['truenorth.StudentExam']", 'symmetrical': 'False'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'full_length_tests': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['truenorth.FullLengthTest']", 'through': u"orm['truenorth.StudentFullLengthTest']", 'symmetrical': 'False'}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'guardian_1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'guardian_1'", 'null': 'True', 'to': u"orm['truenorth.Guardian']"}),
            'guardian_2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'guardian_2'", 'null': 'True', 'to': u"orm['truenorth.Guardian']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'landline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'office_number': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sectional_tests': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['truenorth.SectionalTest']", 'through': u"orm['truenorth.StudentSectionalTest']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '7', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['login.MyUser']", 'unique': 'True'}),
            'worksheets': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['truenorth.Worksheet']", 'through': u"orm['truenorth.StudentWorksheet']", 'symmetrical': 'False'})
        },
        u'truenorth.studentcourse': {
            'Meta': {'object_name': 'StudentCourse'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.Course']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.Student']"})
        },
        u'truenorth.studentexam': {
            'Meta': {'object_name': 'StudentExam'},
            'exam': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.Exam']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scores': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['truenorth.CourseSection']", 'through': u"orm['truenorth.StudentExamSectionScore']", 'symmetrical': 'False'}),
            'skipped': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.Student']"}),
            'taken': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'total_score': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'truenorth.studentexamsectionscore': {
            'Meta': {'object_name': 'StudentExamSectionScore'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.CourseSection']"}),
            'student_exam': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.StudentExam']"})
        },
        u'truenorth.studentfulllengthtest': {
            'Meta': {'object_name': 'StudentFullLengthTest'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'scores': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['truenorth.CourseSection']", 'through': u"orm['truenorth.StudentTestSectionalScore']", 'symmetrical': 'False'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.Student']"}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.FullLengthTest']"})
        },
        u'truenorth.studentsectionaltest': {
            'Meta': {'object_name': 'StudentSectionalTest'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'sectional_test': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.SectionalTest']"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.Student']"})
        },
        u'truenorth.studenttestsectionalscore': {
            'Meta': {'object_name': 'StudentTestSectionalScore'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.CourseSection']"}),
            'student_flt': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.StudentFullLengthTest']"})
        },
        u'truenorth.studentworksheet': {
            'Meta': {'object_name': 'StudentWorksheet'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.Student']"}),
            'worksheet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.Worksheet']"})
        },
        u'truenorth.tutor': {
            'Meta': {'object_name': 'Tutor'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cell_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'landline': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'office_number': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'pan_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['login.MyUser']", 'unique': 'True'})
        },
        u'truenorth.worksheet': {
            'Meta': {'object_name': 'Worksheet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['truenorth.CourseModule']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['truenorth']