from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'Sean M', 
        'title': 'XP news',
        'preview': 'click to read more',
        'content': 'This is a test of a news article',
        'date_posted': 'Today'
    },
    {
        'author': 'Joe V', 
        'title': 'Hotdoggers update',
        'preview': 'click to read more',
        'content': 'This is a test of a news article again',
        'date_posted': 'December 1, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'news/news.html', context)

def story(request):
    
    return render(request, 'news/story.html', {'title': 'Story'})
