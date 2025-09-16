from django.shortcuts import render, redirect
from django.forms import formset_factory
from .ai_wrapper import content_generator
from .models import User, Skill, Experience
from .forms import UserInfoForm, SkillsInfoForm, ExperienceForm


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
            request.session["user_id"] = user.id
            return redirect("skills")
    else:
        form = UserInfoForm()

    return render(
        request,
        "input.html",
        {
            "form": form,
            "heading": "Enter your Info",
            "title": "User Info",
        },
    )


def skills_input(request):

    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("userinfo")
    user = User.objects.get(id=user_id)

    SkillsFormSet = formset_factory(SkillsInfoForm, extra=1)

    if request.method == "POST":
        formset = SkillsFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:

                    # Future feature, adding deletion
                    if form.cleaned_data.get("DELETE"):
                        continue

                    skill = Skill.objects.create(
                        skill_name=form.cleaned_data.get("skill"),
                        skill_proficiency=form.cleaned_data.get("proficiency"),
                        source=form.cleaned_data.get("source"),
                    )
                    skill.user.add(user)

            request.session["skills_completed"] = True
            return redirect("experience")
    else:
        formset = SkillsFormSet()

    return render(
        request,
        "input.html",
        {
            "formset": formset,
            "heading": "Enter your Skills",
            "add_button": "Add skill",
            "title": "Skills",
        },
    )


def experience_input(request):

    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("userinfo")
    user = User.objects.get(id=user_id)

    ExperienceFormSet = formset_factory(ExperienceForm, extra=1)

    if request.method == "POST":
        formset = ExperienceFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    if form.cleaned_data.get("DELETE"):
                        continue

                    Experience.objects.create(
                        user=user,
                        experience_name=form.cleaned_data.get("experience"),
                        start_date=form.cleaned_data.get("start_date"),
                        end_date=form.cleaned_data.get("end_date"),
                        organization=form.cleaned_data.get("organization"),
                        location=form.cleaned_data.get("location"),
                    )
            return redirect("results")
    else:
        formset = ExperienceFormSet()

    return render(
        request,
        "input.html",
        {
            "formset": formset,
            "heading": "Enter your Experience",
            "add_button": "Add Experience",
            "title": "Experience",
        },
    )


def result_page(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("userinfo")
    user = User.objects.get(id=user_id)

    user_form = UserInfoForm(
        initial={
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "link": user.link,
        }
    )

    user_skills = Skill.objects.filter(user=user)
    skills_formset = formset_factory(SkillsInfoForm, extra=0)
    skills_form = skills_formset(
        initial=[
            {
                "skill": skill.skill_name,
                "proficiency": skill.skill_proficiency,
                "source": skill.source,
            }
            for skill in user_skills
        ]
    )

    user_experiences = Experience.objects.filter(user=user)
    experience_formset = formset_factory(ExperienceForm, extra=0)
    experience_form = experience_formset(
        initial=[
            {
                "experience": experience.experience_name,
                "start_date": experience.start_date,
                "end_date": experience.end_date,
                "organization": experience.organization,
                "location": experience.location,
            }
            for experience in user_experiences
        ]
    )

    if request.method == "POST":
        user_form = UserInfoForm(request.POST)
        skills_form = skills_formset(request.POST)
        experience_form = experience_formset(request.POST)

        if (
            user_form.is_valid()
            and skills_form.is_valid()
            and experience_form.is_valid()
        ):
            user.name = user_form.cleaned_data["name"]
            user.email = user_form.cleaned_data["email"]
            user.address = user_form.cleaned_data["address"]
            user.link = user_form.cleaned_data["link"]
            user.save()

            Skill.objects.filter(user=user).delete()
            for form in skills_form:
                if form.cleaned_data:
                    skill = Skill.objects.create(
                        skill_name=form.cleaned_data["skill"],
                        skill_proficiency=form.cleaned_data["proficiency"],
                        source=form.cleaned_data["source"],
                    )
                    skill.user.add(user)

            Experience.objects.filter(user=user).delete()
            for form in experience_form:
                if form.cleaned_data:
                    Experience.objects.create(
                        user=user,
                        experience_name=form.cleaned_data["experience"],
                        start_date=form.cleaned_data["start_date"],
                        end_date=form.cleaned_data["end_date"],
                        organization=form.cleaned_data["organization"],
                        location=form.cleaned_data["location"],
                    )

            return redirect("results")

    return render(
        request,
        "results.html",
        {
            "user_info": user_form,
            "skills_formset": skills_form,
            "experience_formset": experience_form,
        },
    )
