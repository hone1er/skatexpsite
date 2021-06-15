from django.urls import include, path
from . import views
from .views import StaffDetailView, StaffListView

urlpatterns = [
    path('', StaffListView.as_view(), name='staff-main'),
    path("member/<int:pk>/", StaffDetailView.as_view(), name="staff-detail"),

    ]