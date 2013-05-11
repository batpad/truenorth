from django.db import models
from django.contrib.auth.models import User
from ox.django.fields import DictField
from django.conf import settings



class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=7,blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    mobile = models.CharField(max_length=255, blank=True)
    landline = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    # full_name = models.CharField(max_length=255, blank=True)
#    centres = models.ManyToManyField("Centre")
    # centre  = models.CharField(max_length=255, blank=True)
    centre = models.ForeignKey("Centre") # TODO: FIXME
    address = models.TextField(blank=True)
    school = models.CharField(max_length=255, blank=True)
    office_number = models.CharField(max_length=12, blank=True)
    grade = models.CharField(max_length=15, blank=True)
    guardian_1 = models.ForeignKey("Guardian", blank=True, null=True, related_name="guardian_1")    
    guardian_2 = models.ForeignKey("Guardian", blank=True, null=True, related_name="guardian_2")    
    exams = models.ManyToManyField("Exam", through="StudentExam")
    courses = models.ManyToManyField("Course", through="StudentCourse")
    worksheets = models.ManyToManyField("Worksheet", through="StudentWorksheet")
    full_length_tests = models.ManyToManyField("FullLengthTest", through="StudentFullLengthTest")
    sectional_tests = models.ManyToManyField("SectionalTest", through="StudentSectionalTest")
    completed = models.BooleanField(default=False)

    @property
    def get_type(self):
        return self.user.user_type
    @property
    def get_email(self):
        return self.user.email



    def __unicode__(self):
        return ( self.first_name + " " + self.last_name)



class Tutor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=10, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    # full_name = models.CharField(max_length=255, blank=True)
    pan_number = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    cell_number = models.CharField(max_length=255, blank=True)
    landline = models.CharField(max_length=12, blank=True)
    office_number = models.CharField(max_length=12, blank=True)

    @property
    def get_type(self):
        return self.user.user_type
    @property
    def get_email(self):
        return self.user.email



    def __unicode__(self):
        return self.first_name + " " + self.last_name



class Staff(models.Model):
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=10, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    # full_name = models.CharField(max_length=255, blank=True)
    pan_number = models.CharField(max_length=255, blank=True)
    cell_number = models.CharField(max_length=255, blank=True)
    landline = models.CharField(max_length=255, blank=True)
    
    @property
    def get_email(self):
        return self.user.email

    @property
    def get_type(self):
        return self.user.user_type

    
    def __unicode__(self):
        return self.first_name + " " + self.last_name



class Guardian(models.Model):
    '''
        Parent / guardian
    '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    full_name = models.CharField(max_length=255, blank=True)    
    number = models.CharField(max_length=255, blank=True)   
    email = models.CharField(max_length=255, blank=True)   
    

    @property
    def get_type(self):
        return self.user.user_type

    def __unicode__(self):
        return self.full_name

class Centre(models.Model):
    '''
        eg. Colaba, Vile Parle
    '''
    name = models.CharField(max_length=128, unique=True)
    address = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

class Course(models.Model):
    '''
        eg. ACT, SAT, IB
    '''
    name = models.CharField(max_length=64, unique=True)
    total_score = models.IntegerField()

    def __unicode__(self):
        return self.name


class CourseModule(models.Model):
    '''
        Divide course into modules - eg. English, Math
    '''
    name = models.CharField(max_length=64)
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return "%s: %s" % (self.course.name, self.name,)


class CourseSection(models.Model):
    name = models.CharField(max_length=128)
    course = models.ForeignKey(Course)
    total_marks = models.IntegerField()

    def __unicode__(self):
        return "%s: %s" % (self.course.name, self.name,)


class Worksheet(models.Model):
    name = models.CharField(max_length=64)
    module = models.ForeignKey(CourseModule)

    def __unicode__(self):
        return self.name


class StudentWorksheet(models.Model):
    student = models.ForeignKey(Student)
    worksheet = models.ForeignKey(Worksheet)
    completed = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    date = models.DateField()

    def __unicode__(self):
        return "%s: %s" % (self.student.full_name, self.worksheet.name,)
    
class FullLengthTest(models.Model):
    name = models.CharField(max_length=64)
    course = models.ForeignKey(Course)

    def __unicode__(self):
        return "%s: %s" % (self.course.name, self.name,)


class SectionalTest(models.Model):
    name = models.CharField(max_length=128)
    section = models.ForeignKey(CourseSection)

    def __unicode__(self):
        return "%s: %s: %s" % (self.section.course.name, self.section.name, self.name,)

        
class StudentFullLengthTest(models.Model):
    student = models.ForeignKey(Student)
    test = models.ForeignKey(FullLengthTest)    
    scores = models.ManyToManyField(CourseSection, through="StudentTestSectionalScore")
#    score_total = models.IntegerField(null=True)
    notes = models.TextField(blank=True)
    date = models.DateField()

    def __unicode__(self):
        return "%s: %s" % (self.student.full_name, self.test.name,)

class StudentTestSectionalScore(models.Model):
    student_flt = models.ForeignKey(StudentFullLengthTest)
    section = models.ForeignKey("CourseSection")
    score = models.IntegerField()
    

class StudentSectionalTest(models.Model):
    student = models.ForeignKey(Student)
    sectional_test = models.ForeignKey(SectionalTest)
    score = models.IntegerField()
    date = models.DateField()

    def __unicode__(self):
        return "%s: %s" % (self.student.full_name, self.sectional_test.name,)
#    


class Exam(models.Model):
    date = models.DateField()
    course = models.ForeignKey(Course)

    def __unicode__(self):
        dtstring = self.date.strftime("%B, %Y")
        return "%s: %s" % (self.course.name, dtstring,)


class StudentExam(models.Model):
    student = models.ForeignKey(Student)
    exam = models.ForeignKey(Exam)
    scores = models.ManyToManyField(CourseSection, through="StudentExamSectionScore")
#    score_breakup = DictField(default={})
    total_score = models.IntegerField(null=True)
    skipped = models.BooleanField(default=False)
    taken = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s: %s" % (self.student.full_name, self.exam,)


class StudentExamSectionScore(models.Model):
    student_exam = models.ForeignKey(StudentExam)
    section = models.ForeignKey(CourseSection)
    score = models.IntegerField()


class StudentCourse(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    
    def __unicode__(self):
        return "%s: %s" % (self.student.full_name, self.course.name,)

WEEKDAY_CHOICES = (
    (0, 'Sunday'),
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
)

class Batch(models.Model):
    centre = models.ForeignKey("Centre")
    module = models.ForeignKey("CourseModule")
    day = models.IntegerField(choices=WEEKDAY_CHOICES)
    time = models.TimeField()
    tutor  = models.ForeignKey("Tutor")
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Batches"

    def __unicode__(self):
        day = WEEKDAY_CHOICES[self.day][1]
        return " %s at %s on %ss" % (self.module, self.centre, day,)    

class Attendance(models.Model):
    batch = models.ForeignKey(Batch)
    datetime = models.DateTimeField()
    tutor = models.ForeignKey(Tutor)
    students = models.ManyToManyField(Student)

    def __unicode__(self):
        return unicode(self.batch) + " by " + unicode(self.tutor)


class Checkin(models.Model):
    '''
    Model for office staff to simply enter a user (can be student or tutor) and time in. Time-out is optional.
    '''
    centre = models.ForeignKey(Centre)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    time_in = models.DateTimeField() #FIXME: add default for datetime.datetime.now?
    time_out = models.DateTimeField(blank=True, null=True)
    marked_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='marked_checkins')
    

    def __unicode__(self):
        dtstring = self.time_in.strftime("%d %b, %Y at %H:%M")
        return unicode(self.user) + " on " + dtstring

    def get_dict(self):
        return {
            'id': self.id,
            'time_in': self.time_in.strftime("%H:%m"),
            'time_out': self.time_out.strftime("%H:%m") if self.time_out else ''
        }

class Interaction(models.Model):
    '''
    Model for tutor to log an interaction with a student, mentioning time, and some optional notes.
    '''
    tutor = models.ForeignKey(Tutor)
    student = models.ForeignKey(Student)
    datetime = models.DateTimeField() #Q: Add default for now?
    notes = models.TextField(blank=True)
    #Do we need some indication of what course / module this interaction was for?

    def __unicode__(self):
        dtstring = self.time_in.strftime("%d %b, %Y at %H:%M")
        return "%s - %s on %s" % (unicode(self.tutor), unicode(self.student), dtstring)



#class FeedbackSession(models.Model):
#    tutor = models.ForeignKey("Tutor")
#    start_time = models.DateTimeField()
#    duration = models.IntegerField(null=True, help_text="in hours")
#    students = models.ManyToManyField("Student")

#    def __unicode__(self):
#        dtstring = self.start_time.strftime("%d %b, %Y at %H:%M")
#        return "%s: %s" % (self.tutor, dtstring,)
