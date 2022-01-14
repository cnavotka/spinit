from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JoU5pIbrF3EIRuThTNlbbgAiDjgRsCQ7D2x1MOSqFZHcc6qxFhxN5IRDvcqiOMHttWn6L0LJRbrzBMLXfN07Cbk00xYkMU8mr',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
