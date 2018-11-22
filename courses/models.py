# courses/models.py

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Course(models.Model):
    course_number = models.CharField(max_length=10)
    course_name = models.CharField(max_length=50)
    credits = models.FloatField()
    college = models.CharField(max_length=30)
    department = models.CharField(max_length=100)
    pre_reqs = models.CharField(max_length=50)
    course_description = models.TextField()
    course_outcomes = models.TextField()
    course_URL = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return "".format(self.course_number,self.course_name,self.college)

    def get_absolute_url(self):
        return reverse("course_detail", args=[str(self.id)])
