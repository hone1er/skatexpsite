from django.shortcuts import render, redirect
from programs.models import Program
from django.urls import reverse
from .forms import HotdoggerForm, PeWaiver
from .models import Hotdogger, PeProgram
import stripe
import math
from decouple import config
from django.core.mail import EmailMessage


def save_customer(title, request):
    if title == "hot doggers":
        print("hotdog waiver")
        customer_db = Hotdogger()
        customer_db.food_program = False
        customer_db.school = request.POST.get("school")

    else:
        customer_db = PeProgram()
        customer_db.food_program = request.POST.get("food_program") == "on"
        customer_db.student_id = request.POST.get("student_id")

    customer_db.parent = request.POST.get("parent")
    customer_db.phone = request.POST.get("phone_0")
    customer_db.parent_email = request.POST.get("parent_email")
    customer_db.student = request.POST.get("student")
    customer_db.student_email = request.POST.get("student_email")
    customer_db.student_phone = request.POST.get("student_phone_0")
    customer_db.student_grade = request.POST.get("student_grade")
    customer_db.student_address = request.POST.get("student_address")

    customer_db.save()
    return customer_db


# Create your views here.


def hotdoggers(request):
    context = {"programs": Program.objects.filter(title="hot doggers")}
    return render(request, "programs/programs_detail.html", context)


def pe_waiver(request):
    context = {"programs": Program.objects.filter(title="pe waiver program")}
    return render(request, "programs/programs_detail.html", context)


def form(request, program):
    program = Program.objects.filter(title=program)
    form = HotdoggerForm()
    for p in program:
        if p.title == "pe waiver program":
            form = PeWaiver()

    context = {
        "form": form,
        "PUBLIC_STRIPE_KEY": config("PUBLIC_STRIPE_KEY"),
        "program": program,
    }
    return render(request, "programs/form.html", context=context)


def charged(request):
    if request.method == "POST":
        print("Data:", request.POST)
        title = request.POST.get("title")

        cost = float(request.POST.get("cost"))
        donation = float(request.POST.get("amount"))
        amount = int(cost + donation)
        print(amount)
        price_id = None
        stripe_id = request.POST.get("stripe_id")
        for item in stripe.Price.list(product=stripe_id)["data"]:
            if item.unit_amount == amount * 100:
                price_id = item.id
                break
        # save the customer in the Django DB
        customer_db = save_customer(title, request)

        # create the customer in stripe database
        customer = stripe.Customer.create(
            email=request.POST["parent_email"],
            name=request.POST["parent"],
            source=request.POST["stripeToken"],
        )

        # Check if student is enrolled in food program, if not, charge them for the program, otherwise it is no charge
        if customer_db.food_program == False:

            if price_id == None:

                price = stripe.Price.create(
                    unit_amount=amount * 100,
                    currency="usd",
                    product=stripe_id,
                )
                price_id = price.id

            # cost = stripe.Price.retrieve(
            #     price_id,
            # ).unit_amount

            # charge = stripe.Charge.create(
            #     customer=customer,
            #     amount=cost,
            #     currency="usd",
            #     description=f"{customer_db.parent} signed up for {title}",
            # )
            
            order = stripe.Order.create(
                currency="usd",
                customer=customer.id,
                items=[
                    {
                        "type": "sku",
                        "sku": "price_1JPwanAHP5MVK2gMD0l1zEjU",
                        "amount": amount*100
                    },
                ],
            )
            # stripe.Order.pay(order.id)

        # send confirmation email
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
