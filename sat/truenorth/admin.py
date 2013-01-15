from django.contrib import admin
from models import *


class CourseSectionInline(admin.StackedInline):
    model = CourseSection
    extra = 4

class WorksheetInline(admin.StackedInline):
    model = Worksheet
    extra = 5

class FullLengthTestInline(admin.StackedInline):
    model = FullLengthTest
    extra = 5

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['full_name']
    list_filter = ('centre',)
    save_on_top = True

class TutorAdmin(admin.ModelAdmin):
    search_fields = ['full_name']

class CourseAdmin(admin.ModelAdmin):
    save_on_top = True
    inlines = [CourseSectionInline, FullLengthTestInline]

class CourseModuleAdmin(admin.ModelAdmin):
    list_filter = ('course',)
    inlines = [WorksheetInline]

class WorksheetAdmin(admin.ModelAdmin):
    list_filter = ('module',)

class CentreAdmin(admin.ModelAdmin):
    pass

class ExamAdmin(admin.ModelAdmin):
    list_filter = ('course',)
    

class BatchAdmin(admin.ModelAdmin):
    list_filter = ('centre', 'module', 'tutor',)
   

class FullLengthTestAdmin(admin.ModelAdmin):
    list_filter = ('course',)

class SectionalTestAdmin(admin.ModelAdmin):
    list_filter = ('section',)

class AttendanceAdmin(admin.ModelAdmin):
    filter_horizontal = ('students',)
    list_filter = ('students', 'tutor', 'batch',)

class StudentWorksheetAdmin(admin.ModelAdmin):
    list_filter = ('student', 'worksheet', 'completed',)

#class FeedbackSessionAdmin(admin.ModelAdmin):
#    filter_horizontal = ('students',)
#    list_filter = ('tutor', 'students',)

admin.site.register(Student, StudentAdmin)
admin.site.register(Guardian)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(Centre, CentreAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseModule, CourseModuleAdmin)
admin.site.register(Worksheet, WorksheetAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Batch, BatchAdmin)
admin.site.register(FullLengthTest, FullLengthTestAdmin)
admin.site.register(SectionalTest, SectionalTestAdmin)
admin.site.register(StudentWorksheet)
admin.site.register(Attendance, AttendanceAdmin)

#admin.site.register(FeedbackSession, FeedbackSessionAdmin)
