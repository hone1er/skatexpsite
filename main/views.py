from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):

    return render(request, 'main/main.html')

def mission(request):
        return render(request, 'main/mission.html')


