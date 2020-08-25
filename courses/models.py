# courses/models.py

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class College(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=5)
    website = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.abbreviation} {self.name}"

    def get_absolute_url(self):
        return reverse("college_detail", args=[str(self.id)])

class UniversityCourse(models.Model):
    course_number = models.CharField(max_length=10)
    course_name = models.CharField(max_length=50)
    credits = models.FloatField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    pre_reqs = models.CharField(max_length=50)
    course_description = models.TextField()
    course_outcomes = models.TextField()
    course_URL = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ['course_number']

    def __str__(self):
        return "".format(self.course_number, self.course_name, self.college)

    def get_absolute_url(self):
        return reverse("course_detail", args=[str(self.id)])

class CommunityCollegeCourse(models.Model):
    course_number = models.CharField(max_length=10)
    course_name = models.CharField(max_length=50)
    credits = models.FloatField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    course_equivalent = models.ManyToManyField(UniversityCourse)
    department = models.CharField(max_length=100)
    pre_reqs = models.CharField(max_length=50)
    course_description = models.TextField()
    course_outcomes = models.TextField()
    course_URL = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ['course_number']

    def __str__(self):
        return "".format(self.course_number, self.course_name, self.college)

    def get_absolute_url(self):
        return reverse("course_detail", args=[str(self.id)])


class Major(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=5)
    website = models.URLField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    community_college_courses = models.ManyToManyField(CommunityCollegeCourse)
    university_courses = models.ManyToManyField(UniversityCourse)
    date_added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ['abbreviation']

    def __str__(self):
        return " ".format(self.abbreviation, self.name, self.college)

    def get_absolute_url(self):
        return reverse("major_detail", args=[str(self.id)])
