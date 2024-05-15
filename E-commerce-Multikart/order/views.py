from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from order.models import Cart
from django.shortcuts import get_object_or_404

from paypal.standard.forms import PayPalPaymentsForm
from django.template.defaultfilters import floatformat
from django.conf import settings
import uuid
from django.urls import reverse
from accounts.models import ShippingAdress

# Create your views here.

@login_required
def cart(request):
    cart = Cart.objects.filter(user=request.user)
    
    context = {
        'cart' : cart
    }
    return render(request, 'cart.html' , context)


def checkout(request):
    host = request.get_host()
    user = request.user
    total_price = user.get_total_cards_price()
    shipping= ShippingAdress.objects.filter(user=request.user).first()

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount' : str(total_price),
        'item_name' : 'checkout',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url' : f"http://{host}{reverse('paypal-ipn')}",
        'return_url' : f"http://{host}{reverse('order_success')}",
        'cancel_url' : f"http://{host}{reverse('cart_page')}",
    }

    # PayPalPaymentsForm for rendering PayPal payment form
    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)
        
    context = {
        'paypal': paypal_payment,
        'shipping': shipping
    }

    return render(request, 'checkout.html', context)

def order_success(request):
    shipping= ShippingAdress.objects.filter(user=request.user).first()

    context = {

        'shipping': shipping

    }
    return render(request, 'order-success.html',context)


