from django.shortcuts import render
from programs.models import Program
from django.views.generic import ListView, DetailView
# Create your views here.

class ProgramListView(ListView):
    model = Program
    template_name = 'programs/programs.html'
    context_object_name = 'programs'
    ordering = ['-date_posted']



def pe_waiver(request):
    context = {
        'programs': Program.objects.filter(title="pe waiver program")
    }
    return render(request, 'programs/pe_waiver.html', context)

def hotdoggers(request):
    context = {
        'programs': Program.objects.filter(title="hotdoggers")
    }
    return render(request, 'programs/hotdoggers.html', context)