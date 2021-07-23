from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from decouple import config


import stripe

stripe.api_key = config("STRIPE_KEY")

# Create your views here.


def donate(request):

    return render(
        request,
        "donate/donate.html",
        context={"PUBLIC_STRIPE_KEY": config("PUBLIC_STRIPE_KEY")},
    )


def charge(request):
	if request.method == "POST":
		print("Data:", request.POST)
		amount = int(request.POST["amount"])
		frequency = request.POST["frequency"]
		price_id = None
		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['name'],
			source=request.POST['stripeToken']
			)
		for item in stripe.Price.list(product="prod_JoiTIagNrRn2Vw")["data"]:
			if item.unit_amount == amount*100:
				price_id = item.id
				break
		if frequency == "monthly":
			# check if price exist, if not create a subscription with new price
			if price_id:
				subscription = stripe.Subscription.create(
					customer=customer.id,
					items=[{"price": price_id},],)

			else:
				price = stripe.Price.create(
					unit_amount=amount * 100,
					currency="usd",
					recurring={"interval": "month"},
					product="prod_JoiTIagNrRn2Vw",
				)
				subscription = stripe.Subscription.create(
					customer=customer.id,
					items=[{"price": stripe.Price.retrieve(price.id)},],)
		else:
			charge = stripe.Charge.create(
				customer=customer,
				amount=amount*100,
				currency='usd',
				description=f"Donation to Skate XP - {request.POST['name']}"
				)
	return redirect(reverse("success", args=[amount]))


def successMsg(request, args):
    amount = args
    return render(request, "donate/success.html", {"amount": amount})
