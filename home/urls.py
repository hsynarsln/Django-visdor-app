from django.urls import path

from .views import about, home, teacher

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("teachers/", teacher, name="teacher"),
]
