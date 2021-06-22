from django.urls import include, path
from . import views
from .views import ProgramListView

urlpatterns = [
    path("", ProgramListView.as_view(), name="program-home"),
    path("hotdoggers/", views.hotdoggers, name="hotdoggers"),
    path("pe_waiver/", views.pe_waiver, name="pe-program"),
    
]
