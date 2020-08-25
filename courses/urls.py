# courses/urls.py

from django.urls import path

from .views import CommunityCollegeCourseListView

urlpatterns = [path("", CommunityCollegeCourseListView.as_view(), name="course_list")]
