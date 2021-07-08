from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from decouple import config



import stripe

stripe.api_key = config("STRIPE_KEY")

# Create your views here.

def donate(request):

	return render(request, 'donate/donate.html',context={
        'PUBLIC_STRIPE_KEY': config('PUBLIC_STRIPE_KEY')})


def charge(request):
	if request.method == 'POST':
		print('Data:', request.POST)
		amount = int(request.POST['amount'])
		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['name'],
			source=request.POST['stripeToken']
			)
		# if not request.POST['sub']:
		# 	subscription = stripe.Subscription.create(
		# 				customer=customer.get('id'),
		# 				items=[{
		# 					'price': amount,
		# 				}],
		# 				payment_behavior='default_incomplete',
		# 				expand=['latest_invoice.payment_intent'],
		# 			)



		# else:

		charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='usd',
			description=f"Donation to Skate XP - {request.POST['name']}"
			)
		

	return redirect(reverse('success', args=[amount]))




def successMsg(request, args):
	amount = args
	return render(request, 'donate/success.html', {'amount':amount})