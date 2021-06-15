from staff.models import Staff
from django.shortcuts import render
from staff.models import Staff
from django.views.generic import ListView, DetailView
# Create your views here.

class StaffListView(ListView):
    model = Staff
    template_name = 'staff/staff.html'
    context_object_name = 'staff'



class StaffDetailView(DetailView):
    model = Staff




