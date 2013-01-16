from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from sat.login import *


class UserProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    list_display = ('id', 'username', 'full_name', 'email', 'location',
        'preflang', 'featured', 'created_on')
    list_filter = list_display[5:]
    search_fields = list_display[:5]


class TaggedProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')

#admin.site.register(login, UserProfileAdmin)
#admin.site.register(TaggedProfile, TaggedProfileAdmin)
