from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("userinfo/", views.userinfo_input, name="userinfo"),
    path("skills/", views.skills_input, name="skills"),
    path("experience/", views.experience_input, name="experience"),
    path("results/", views.result_page, name="results"),
]
