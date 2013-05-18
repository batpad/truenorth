# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Staff.address'
        db.add_column(u'truenorth_staff', 'address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Staff.address'
        db.delete_column(u'truenorth_staff', 'address')


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
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
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