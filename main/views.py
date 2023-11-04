from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):

    return render(request, "main/main.html")


def mission(request):
    return render(request, "main/mission.html")


def solutions(request):
    return render(request, "main/solutions.html")


def special_events(request):
    return render(request, "main/events.html")
