from django.shortcuts import render
from story.models import Story
from django.views.generic import ListView, DetailView
# Create your views here.


class StoryListView(ListView):
    model = Story
    template_name = 'story/story.html'
    context_object_name = 'storys'
    ordering = ['-date_posted']



class StoryDetailView(DetailView):
    model = Story

