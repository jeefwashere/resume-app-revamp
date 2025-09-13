from django.shortcuts import render, redirect
from django.forms import formset_factory
from .ai_wrapper import content_generator
from .models import User, Skill
from .forms import UserInfoForm, SkillsInfoForm


# Create your views here.
def index(request):
    return render(request, "index.html")


def ai_prompter(request):
    result = None
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        result = content_generator(user_input)
    return render(request, "prompt.html", {"result": result})


def userinfo_input(request):
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                address=form.cleaned_data["address"],
                link=form.cleaned_data["link"],
            )
            return redirect("skills")
    else:
        form = UserInfoForm()

    return render(request, "input.html", {"form": form, "heading": "Enter your Info"})


def skills_input(request):
    SkillsFormSet = formset_factory(SkillsInfoForm, extra=1)

    if request.method == "POST":
        formset = SkillsFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    Skill.objects.create(
                        skill_name=form.cleaned_data.get("skill"),
                        skill_proficiency=form.cleaned_data.get("proficiency"),
                        source=form.cleaned_data.get("source"),
                    )
            return redirect("experience")
        # If not valid, fall through to render below
    else:
        formset = SkillsFormSet()

    return render(
        request,
        "input.html",
        {"formset": formset, "heading": "Enter your Skills"},
    )

def experience_input(request):
    