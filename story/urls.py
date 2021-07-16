from django.urls import include, path
from . import views
from .views import StoryDetailView, StoryListView

urlpatterns = [
    path("", StoryListView.as_view(), name="story"),
    path("story/<int:pk>/", StoryDetailView.as_view(), name="story-detail"),

]
