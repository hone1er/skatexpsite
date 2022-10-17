from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("hotdoggers/", views.hotdoggers, name="hotdoggers"),
    path("pe_waiver/", views.pe_waiver, name="pe-program"),
    path("sk8xp_van_tours/", views.sk8xp_van_tours, name="van-tour"),
    path("form/<program>", views.form, name="form"),
    path("form/", views.form, name="form"),
    path("charged/", views.charged, name="charged"),
    path("successProgram/<str:args>", views.successMsg, name="successProgram"),
    path("ajax/validate_coupon/", views.validate_coupon, name="validate_coupon"),
    path(
        "ajax/validate_coupon/<str:args>", views.validate_coupon, name="validate_coupon"
    ),
]
