# courses/views.py

from django.shortcuts import render
from django.views.generic import ListView

from .models import CommunityCollegeCourse


class CommunityCollegeCourseListView(ListView):
    model = CommunityCollegeCourse
    template_name = "courses/course_list.html"
