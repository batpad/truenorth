from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from sat.truenorth.models import *


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
        ('4', 'STAFF')
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

    def get_category(self):
        return self.user_type

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

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
