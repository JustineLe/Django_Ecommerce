from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from product.models import Product
from .cart import Cart


# Create your views here.
def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'cart/menu_cart.html')


def carts(request):
    return render(request, 'cart/carts.html')


@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')


def hx_menu_cart(request):
    return render(request, 'cart/menu_cart.html')


def update_cart(request, product_id, action):
    cart = Cart(request)

    if action == 'increment':
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)

    product = Product.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)['quantity']

    item = {
        'product': {
            'id': product.id,
            'name': product.name,
            'image': product.image,
            'get_thumbnail': product.get_thumbnail(),
            'price': product.price,
        },
        'total_price': (quantity * product.price),
        'quantity': quantity
    }

    response = render(request, 'cart/partials/cart_items.html', {'item': item})
    response['HX-Trigger'] = 'update-menu-cart'

    return response


def hx_cart_total(request):
    return render(request, 'cart/partials/cart_total.html')

