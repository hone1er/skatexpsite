from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.home, name='news-home'),
    path('story', views.story, name='news-story'),

    ]