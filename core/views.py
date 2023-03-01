from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import login

from core.forms import SignUpForm
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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})


@login_required
def my_account(request):
    return render(request, 'core/my_account.html')


@login_required
def edit_my_account(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')

        user = request.user

        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.save()

        return redirect('my_account')

    return render(request, 'core/edit_my_account.html')
