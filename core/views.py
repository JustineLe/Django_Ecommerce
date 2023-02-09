from django.shortcuts import render
from django.db.models import Q

from product.models import Product, Category


# Create your views here.
def frontpage(request):
    products = Product.objects.all()[:10]

    return render(request, 'core/frontpage.html', {
        "products": products
    })


def shop(request):
    active_category = request.GET.get('category', '')
    search = request.GET.get('search', '')

    categories = Category.objects.all()
    products = Product.objects.all()

    if active_category:
        products = products.filter(category__slug=active_category)

    if search:
        products = products.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search) |
            Q(slug__icontains=search)
        )

    context = {
        "categories": categories,
        "products": products,
        "active_category": active_category
    }

    return render(request, 'core/shop.html', context)
