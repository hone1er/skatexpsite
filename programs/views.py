from django.shortcuts import render
from programs.models import Program
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect




# Create your views here.


class ProgramListView(ListView):
    model = Program
    template_name = "programs/programs.html"
    context_object_name = "programs"


class ProgramDetailView(DetailView):
    model = Program




# def pe_waiver(request):
#     if request.method == "POST":
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect("/thanks/")

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
#     context = {"programs": Program.objects.filter(title="pe waiver program"), form: form}
#     return render(request, "programs/pe_waiver.html", context)


def hotdoggers(request):
    context = {"programs": Program.objects.filter(title="hotdoggers")}
    return render(request, "programs/hotdoggers.html", context)

def pe_waiver(request):
    context = {"programs": Program.objects.filter(title="pe waiver program")}
    return render(request, "programs/programs_detail.html", context)