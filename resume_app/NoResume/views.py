from django.shortcuts import render, redirect
from .ai_wrapper import content_generator


# Create your views here.
def index(request):
    return render(request, "index.html")


def ai_prompter(request):
    result = None
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        result = content_generator(user_input)
    return render(request, "prompt.html", {"result": result})
