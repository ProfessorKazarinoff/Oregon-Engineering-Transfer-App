# pages/urls.py

from django.urls import path
from .views import HomePageView, AboutPageView, StartPageView

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("start/", StartPageView.as_view(), name="start"),
    path("", HomePageView.as_view(), name="home"),
]
