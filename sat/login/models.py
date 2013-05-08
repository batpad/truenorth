from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from sat.truenorth.models import *
from sat.login.first_last_days import get_month_day_range
import datetime

class MyUserManager(BaseUserManager):
    def create_user(self, email, user_type='', password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=MyUserManager.normalize_email(email),
            user_type=user_type.upper(),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email, password=password,)
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        db_index=True,
    )

    usertype =(
        ('1', 'TEACHER'),
        ('2', 'STUDENT'),
        ('3', 'GAURDIAN'),
        ('4', 'STAFF'),
               ) 


#    user_type = models.CharField(max_length=10, choices=usertype)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    @property
    def user_type(self):
        if Student.objects.filter(user=self).count() > 0:
            return 'student'
        elif Tutor.objects.filter(user=self).count() > 0:
            return 'tutor'
        elif Guardian.objects.filter(user=self).count() > 0:
            return 'guardian'
        elif Staff.objects.filter(user=self).count() > 0:
            return 'superuser'
        elif self.is_admin:
            return 'admin'
        elif self.is_staff:
            return 'staff'
        else:
            return 'unknown'
    def last_week_attendance_count():
        start_date = datetime.datetime.now()
        end_date = datetime.timedelta(days=7)
        attendance = get_attendance_between_dates(start_date,end_date)
        return attendance.count()
    def get_all_attendance():
        atten
        

    def get_category(self):
        return self.user_type

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email
    def get_attendance_between_dates(self,start_date,end_date):
        return Checkin.objects.filter(user = self,time_in__range = (start_date,end_date))

    def get_attendance(self, date):
        day_min = datetime.datetime.combine(date, datetime.time.min)
        day_max = datetime.datetime.combine(date, datetime.time.max)
        qset = Checkin.objects.filter(user=self).filter(time_in__range=(day_min, day_max))
        if qset.count() > 0:
            return qset[0]
        else:
            return False

    def get_attendance_data(self, date=datetime.datetime.today()):
        checkin = self.get_attendance(date)
        d = {'checkin': checkin}
        if self.user_type == 'student':
            d['student'] = Student.objects.get(user=self)
        if self.user_type == 'tutor':
            d['tutor'] = Tutor.objects.get(user=self)
        return d

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
