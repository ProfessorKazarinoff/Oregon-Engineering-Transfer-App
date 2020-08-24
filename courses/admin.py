# courses/admin.py

from django.contrib import admin

from .models import Course, College, Major

admin.site.register(Course)
admin.site.register(College)
admin.site.register(Major)
