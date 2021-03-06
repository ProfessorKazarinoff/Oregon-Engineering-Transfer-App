# courses/views.py

from django.shortcuts import render
from django.views.generic import ListView

from .models import CommunityCollegeCourse, Major


class CommunityCollegeCourseListView(ListView):
    model = CommunityCollegeCourse
    template_name = "courses/course_list.html"

class MajorListView(ListView):
    model = Major
    template_name = "courses/major_list.html"
