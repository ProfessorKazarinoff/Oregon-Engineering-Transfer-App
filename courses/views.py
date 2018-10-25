# courses/views.py

from django.shortcuts import render
from django.views.generic import ListView

from .models import Course


class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
