from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.home, name='main-home'),
    path('mission/', views.mission, name='main-mission'),

    ]