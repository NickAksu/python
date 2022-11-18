from sqlite3 import Time
from django.contrib import admin

from .models import Subject, Timetable

admin.site.register(Subject)
admin.site.register(Timetable)
