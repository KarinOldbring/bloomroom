from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    """
    Prevents entering checkout with empty bag
    """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'Your shopping bag is empty at the moment!')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LH1usB2umrtcVfVDEzUpirv8dDV2UiLJHd06Ec8garzhyd5Eu5lilKoLWM1tj9CLZy8X3cRaqwvW622VFT473QU00xR0MHTmJ',
        'client_secret': 'test client_secret'
    }

    return render(request, template, context)
