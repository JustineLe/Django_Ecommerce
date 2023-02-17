from django.shortcuts import render, get_object_or_404

from product.models import Product


# Create your views here.
def product(request, slug):
    products = get_object_or_404(Product, slug=slug)

    context = {
        "products": products
    }

    return render(request, 'product/product.html', context)
