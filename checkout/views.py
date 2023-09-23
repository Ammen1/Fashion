import chapa
from django.shortcuts import redirect
from django.http import HttpResponse

from django.http import JsonResponse
import json

from account.models import Address
from basket.basket import Basket
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from orders.models import Order, OrderItem

import http.client
import json

from .models import DeliveryOptions


@login_required
def deliverychoices(request):
    deliveryoptions = DeliveryOptions.objects.filter(is_active=True)
    return render(request, "checkout/delivery_choices.html", {"deliveryoptions": deliveryoptions})


@login_required
def basket_update_delivery(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        delivery_option = int(request.POST.get("deliveryoption"))
        delivery_type = DeliveryOptions.objects.get(id=delivery_option)
        updated_total_price = basket.basket_update_delivery(delivery_type.delivery_price)

        session = request.session
        if "purchase" not in request.session:
            session["purchase"] = {
                "delivery_id": delivery_type.id,
            }
        else:
            session["purchase"]["delivery_id"] = delivery_type.id
            session.modified = True

        response = JsonResponse({"total": updated_total_price, "delivery_price": delivery_type.delivery_price})
        return response


@login_required
def delivery_address(request):

    session = request.session
    if "purchase" not in request.session:
        messages.success(request, "Please select delivery option")
        return HttpResponseRedirect(request.META["HTTP_REFERER"])

    addresses = Address.objects.filter(customer=request.user).order_by("-default")

    if "address" not in request.session:
        session["address"] = {"address_id": str(addresses[0].id)}
    else:
        session["address"]["address_id"] = str(addresses[0].id)
        session.modified = True

    return render(request, "checkout/delivery_address.html", {"addresses": addresses})


@login_required
def payment_selection(request):

    session = request.session
    if "address" not in session:
        messages.success(request, "Please select address option")
        return HttpResponseRedirect(request.META["HTTP_REFERER"])

    return render(request, "checkout/payment_selection.html", {})


@login_required
def payment_complete(request):
    chapa_api = ChapaAPI()

    body = json.loads(request.body)
    order_id = body["orderID"]
    user_id = request.user.id

    # Use the ChapaAPI to verify the payment
    transaction = api.verify_payment(order_id)

    if transaction.get('status') == 'success':
        total_paid = transaction.get('amount')

        # Create the order using Chapa transaction details
        # Replace the attributes with appropriate Chapa transaction data
        order = Order.objects.create(
            user_id=user_id,
            full_name=transaction.get('full_name'),
            email=transaction.get('email'),
            address1=transaction.get('address_line_1'),
            address2=transaction.get('address_line_2'),
            postal_code=transaction.get('postal_code'),
            country_code=transaction.get('country_code'),
            total_paid=total_paid,
            order_key=order_id,
            payment_option="chapa",
            billing_status=True,
        )

        order_id = order.pk

        # Create order items using Chapa transaction data
        basket = Basket(request)
        for item in basket:
            OrderItem.objects.create(
                order_id=order_id,
                product=item["product"],
                price=item["price"],
                quantity=item["qty"]
            )

        return JsonResponse("Payment completed!", safe=False)
    else:
        return JsonResponse("Payment verification failed!", status=400)


@login_required
def payment_successful(request):
    basket = Basket(request)
    basket.clear()
    return render(request, "checkout/payment_successful.html", {})


def pay_chapa(request):
    conn = http.client.HTTPSConnection("api.chapa.co")
    payload = json.dumps({
        "amount": "10",
        "currency": "ETB",
        "email": "amenguda@gmail.com",
        "first_name": "Amen",
        "last_name": "Guda",
        "phone_number": "0944365493",
        "tx_ref": "chewat",
        "callback_url": "http://127.0.0.1:8000/",
        "return_url": "http://127.0.0.1:8000/",
        "customization[title]": "Payment ",
        "customization[description]": "I love "
    })
    headers = {
        'Authorization': 'Bearer CHASECK_TEST-fsztr4z05gWYzxkyYVQQWyij1kzjqFUw',
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/v1/transaction/initialize", payload, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")

    # Process the response and return an appropriate HTTP response
    if res.status == 200:
        response_data = json.loads(data)
        checkout_url = response_data["data"]["checkout_url"]
        return redirect(checkout_url)
        # Successful response
    else:
        return HttpResponse("Payment initiation failed")  # Error response


# import requests
# from django.conf import settings
# from django.shortcuts import redirect

# import http.client
# import json
# import requests
# from django.conf import settings
# from django.http import HttpResponse
# from django.shortcuts import redirect

# def initiate_payment(request):
#     # Get the amount to be paid from the form data
#     amount = request.POST.get('amount')

#     # Create a payment request to Chapa
#     payload = {
#         'public_key': settings.CHAPA_PUBLIC_KEY,
#         "amount": "100",
#         "currency": "ETB",
#         "email": "amenguda@gmail.com",

#         # ...
#     }
#     headers = {
#         'Authorization': f'Bearer {settings.CHAPA_SECRET}',
#         'Content-Type': 'application/json'
#     }

#     conn = http.client.HTTPSConnection("api.chapa.co")
#     conn.request("POST", "/v1/transaction/initialize", json.dumps(payload), headers)
#     res = conn.getresponse()
#     data = res.read().decode("utf-8")

#     # Redirect the user to the Chapa payment page
#     if res.status == 200:
#         response_data = json.loads(data)
#         checkout_url = response_data["data"]["checkout_url"]
#         return redirect(checkout_url)
#     else:
#         return HttpResponse("Payment initiation failed")


# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse

# @csrf_exempt
# def chapa_webhook(request):
#     if request.method == 'POST':
#         # Handle the Chapa webhook logic
#         # ...

#         return HttpResponse(status=200)
#     else:
#         return HttpResponse(status=405)  # Method not allowed


def chapa_view(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        result = chapa.response_data["data"]["checkout_url"]
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Invalid request method'})
