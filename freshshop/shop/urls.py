from django.urls import path
from . import views as shop
from django.urls import reverse
from django.shortcuts import redirect

urlpatterns = [
    path("", shop.shop, name="shop"),
    path("shop_detail/", shop.shop_detail, name="shop_detail"),
    path("cart/", shop.cart, name="cart"),
    path("checkout/", shop.checkout, name="checkout"),
    path("my_account/", shop.my_account, name="my_account"),
    path("wishlist/", shop.wishlist, name="wishlist")
]