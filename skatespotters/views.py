from django.shortcuts import render

# Create your views here.
def skatespotters(request):
        return render(request, 'skatespotters/skatespotters.html')