from django.shortcuts import render, redirect
from programs.models import Program
from django.urls import reverse
from .forms import CustomerForm
from .models import Customer
import stripe
import math
from decouple import config
from django.core.mail import EmailMessage


# Create your views here.


def hotdoggers(request):
    context = {"programs": Program.objects.filter(title="hotdoggers")}
    return render(request, "programs/programs_detail.html", context)


def pe_waiver(request):
    context = {"programs": Program.objects.filter(title="pe waiver program")}
    return render(request, "programs/programs_detail.html", context)


def form(request, program):
    form = CustomerForm()
    context = {
        "form": form,
        "PUBLIC_STRIPE_KEY": config("PUBLIC_STRIPE_KEY"),
        "program": Program.objects.filter(title=program),
    }
    print(context["program"])
    return render(request, "programs/form.html", context=context)


def charged(request):

    if request.method == "POST":
        customer_db = Customer()
        customer_db.parent = request.POST.get("parent")
        customer_db.phone = request.POST.get("phone_0")
        customer_db.parent_email = request.POST.get("parent_email")
        customer_db.student = request.POST.get("student")
        customer_db.student_email = request.POST.get("student_email")
        customer_db.student_phone = request.POST.get("student_phone_0")
        customer_db.student_grade = request.POST.get("student_grade")
        customer_db.student_address = request.POST.get("student_address")
        customer_db.save()

        stripe_id = request.POST.get("stripe_id")
        cost = stripe.Price.retrieve(
            stripe_id,
        ).unit_amount
        # cost = request.POST.get("cost")
        title = request.POST.get("title")
        print("Data:", request.POST)

        customer = stripe.Customer.create(
            email=request.POST["parent_email"],
            name=request.POST["parent"],
            source=request.POST["stripeToken"],
        )
        # # if not request.POST['sub']:
        # # 	subscription = stripe.Subscription.create(
        # # 				customer=customer.get('id'),
        # # 				items=[{
        # # 					'price': amount,
        # # 				}],
        # # 				payment_behavior='default_incomplete',
        # # 				expand=['latest_invoice.payment_intent'],
        # # 			)

        # else:
        charge = stripe.Charge.create(
            customer=customer,
            amount=cost,
            currency="usd",
            description=f"{customer_db.parent} signed up for {title}",
        )
        email = EmailMessage(
            f"You signed up for the {title}!",
            f"Thank you for signing up for the {title}! If you have any questions, reach out to us anytime at info@skatexp.org!",
            "skatexp.org" + "<info@skatexp.org>",
            [customer_db.parent_email],
            headers={"Reply-To": "info@skatexp.org"},
        )
        email.send()

    return redirect(reverse("successProgram", args=[title]))


def successMsg(request, args):
    title = args
    return render(request, "programs/success.html", {"title": title})
