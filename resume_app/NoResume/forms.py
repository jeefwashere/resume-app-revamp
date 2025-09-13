from django import forms
from . import models


class UserInfoForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    address = forms.CharField(max_length=100, required=True)
    link = forms.URLField(required=False)


class SkillsInfoForm(forms.Form):
    skill = forms.CharField(max_length=100, required=True)
    PROFICIENCY_CHOICES = [
        (None, "--"),
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
        ("expert", "Expert"),
    ]
    proficiency = forms.ChoiceField(choices=PROFICIENCY_CHOICES, required=False)
    source = forms.CharField(max_length=100, required=True)


class ExperienceForm(forms.Form):
    experience = forms.CharField(max_length=100, required=True)
    start_date = forms.DateField(required=True)
    end_date = forms.DateField(required=True)
    organization = forms.CharField(max_length=100, required=True)
    location = forms.CharField(max_length=100, required=False)
