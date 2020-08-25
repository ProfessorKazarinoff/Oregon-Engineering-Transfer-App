# courses/admin.py

from django.contrib import admin

from .models import UniversityCourse,CommunityCollegeCourse, College, Major

admin.site.register(CommunityCollegeCourse)
admin.site.register(UniversityCourse)
admin.site.register(College)
admin.site.register(Major)
