from django.urls import include, path
from . import views

urlpatterns = [
    path("hotdoggers/", views.hotdoggers, name="hotdoggers"),
    path("pe_waiver/", views.pe_waiver, name="pe-program"),
    path("form/<program>", views.form, name="form"),
    path("form/", views.form, name="form"),
    path("charged/", views.charged, name="charged"),
    path('successProgram/<str:args>', views.successMsg, name="successProgram"),
    
]
