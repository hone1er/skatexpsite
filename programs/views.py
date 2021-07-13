from django.shortcuts import render
from programs.models import Program
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect
from .forms import CustomerForm
from .models import Customer



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
    return render(request, "programs/programs_detail.html", context)

def pe_waiver(request):
    context = {"programs": Program.objects.filter(title="pe waiver program")}
    return render(request, "programs/programs_detail.html", context)

def form(request):
    if request.method == 'POST':
            customer = Customer()
            print(request.POST)
            customer.parent = request.POST.get('parent')
            customer.phone = request.POST.get('phone_0')
            customer.parent_email = request.POST.get('parent_email')
            customer.student = request.POST.get('student')
            customer.student_email = request.POST.get('student_email')
            customer.student_phone = request.POST.get('student_phone_0')
            customer.student_grade = request.POST.get('student_grade')
            customer.student_address = request.POST.get('student_address')
            customer.save()
            return HttpResponseRedirect("https://buy.stripe.com/test_eVadTSbBvcjp9Y4288")
    form = CustomerForm()
    context = {'form': form}
    return render(request, 'programs/form.html', context=context)


