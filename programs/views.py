from django.shortcuts import render, redirect
from programs.models import Program
from django.urls import reverse
from .forms import HotdoggerForm, PeWaiver
from .models import Hotdogger, PeProgram, Coupon
import stripe
import math
from decouple import config
from django.core.mail import EmailMessage
from django.http import JsonResponse


def save_customer(title, request):
    if title == "hot doggers":
        print("hotdog waiver")
        customer_db = Hotdogger()
        customer_db.food_program = False
        customer_db.school = request.POST.get("school")

    else:
        customer_db = PeProgram()
        customer_db.food_program = request.POST.get("food_program") == "on"
        customer_db.skater_id = request.POST.get("skater_id")

    customer_db.parent = request.POST.get("parent")
    customer_db.phone = request.POST.get("phone_0")
    customer_db.parent_email = request.POST.get("parent_email")
    customer_db.parent_address = request.POST.get("parent_address")
    customer_db.skater = request.POST.get("skater")
    customer_db.skater_email = request.POST.get("skater_email")
    customer_db.skater_phone = request.POST.get("skater_phone_0")
    customer_db.skater_grade = request.POST.get("skater_grade")
    customer_db.coupon = request.POST.get("coupon")


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
        donation = float(request.POST.get("donation_amount"))
        amount = float(cost + donation)
        print(amount)
        
        # save the customer in the Django DB
        customer_db = save_customer(title, request)

        # create the customer in stripe database
        customer = stripe.Customer.create(
            email=request.POST["parent_email"],
            name=request.POST["parent"],
            source=request.POST["stripeToken"],
        )

        # Check if skater is enrolled in food program, if not, charge them for the program, otherwise it is no charge
        if customer_db.food_program == False:


            charge = stripe.Charge.create(
                customer=customer,
                amount=int(amount *100),
                currency="usd",
                description=f"{customer_db.parent} signed up for {title}",
            )
        elif customer_db.food_program == True and int(donation) > 0:
            charge = stripe.Charge.create(
                customer=customer,
                amount=int(float(donation) *100),
                currency="usd",
                description=f"{customer_db.parent} signed up for {title}",)
            
            
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



def validate_coupon(request):
    coupon_code = request.GET.get('coupon', None)
    coupon = False
    discount = None
    if Coupon.objects.filter(code=coupon_code):
        coupon = True
        for obj in Coupon.objects.filter(code=coupon_code):
            discount = obj.amount_off
            break
    data = {
        'coupon': coupon,
        'discount': discount
    }
    return JsonResponse(data)