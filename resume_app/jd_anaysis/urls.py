from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="jd_index"),
]

