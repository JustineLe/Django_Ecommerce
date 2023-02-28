from django.urls import path

from cart.views import add_to_cart, carts, checkout

urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('', carts, name='cart'),
    path('checkout/', checkout, name='checkout'),
]