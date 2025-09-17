from django import forms
from . import models


class DatePicker(forms.DateInput):
    input_type = "date"


class UserInfoForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    address = forms.CharField(max_length=100, required=True)
    link = forms.URLField(required=False)


class SkillsInfoForm(forms.Form):
    skill = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"required": "required"}),
    )
    PROFICIENCY_CHOICES = [
        (None, "--"),
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
        ("expert", "Expert"),
    ]
    proficiency = forms.ChoiceField(choices=PROFICIENCY_CHOICES, required=False)
    source = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"required": "required"}),
    )


class ExperienceForm(forms.Form):
    experience = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"required": "required"}),
    )
    start_date = forms.DateField(
        required=True,
        widget=DatePicker(attrs={"required": "required"}),
    )
    end_date = forms.DateField(
        required=True,
        widget=DatePicker(attrs={"required": "required"}),
    )
    organization = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"required": "required"}),
    )
    location = forms.CharField(max_length=100, required=False)


class ResultsForm(UserInfoForm, SkillsInfoForm, ExperienceForm):
    pass
