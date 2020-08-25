# courses/urls.py

from django.urls import path

from .views import CommunityCollegeCourseListView, MajorListView

urlpatterns = [
    path("list", CommunityCollegeCourseListView.as_view(), name="course_list"),
    path("majors", MajorListView.as_view(), name="major_list"),
]
