from django.shortcuts import render
from news.models import Post
from django.views.generic import ListView, DetailView
# Create your views here.



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'news/news.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post


