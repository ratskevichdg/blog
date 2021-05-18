from django.shortcuts import render


def shop(request):
    return render(request, "shop.html", {})


def shop_detail(request):
    return render(request, "shop_detail.html", {})


def cart(request):
    return render(request, "cart.html", {})


def checkout(request):
    return render(request, "checkout.html", {})


def my_account(request):
    return render(request, "my_account.html", {})


def wishlist(request):
    return render(request, "wishlist.html", {})
