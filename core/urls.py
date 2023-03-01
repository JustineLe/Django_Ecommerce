from django.contrib.auth import views
from django.urls import path

from core.views import frontpage, signup, shop, my_account, edit_my_account
from product.views import product

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),

    # Authentication url
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('myaccount/', my_account, name='my_account'),
    path('editmyaccount/', edit_my_account, name='edit_my_account'),
]
