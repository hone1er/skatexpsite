from django.urls import include, path
from . import views
from .views import PostDetailView, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="news-home"),
    path("story/<int:pk>/", PostDetailView.as_view(), name="post-detail"),

]
