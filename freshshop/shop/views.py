from django.shortcuts import render


def shop(request):
    context = {"page_name": "shop"}
    return render(request, "shop.html", context)


def shop_detail(request):
    context = {"page_name": "shop detail"}
    return render(request, "shop_detail.html", context)


def cart(request):
    context = {"page_name": "cart"}
    return render(request, "cart.html", context)


def checkout(request):
    context = {"page_name": "checkout"}
    return render(request, "checkout.html", context)


def my_account(request):
    context = {"page_name": "my account"}
    return render(request, "my_account.html", context)


def wishlist(request):
    context = {"page_name": "wishlist"}
    return render(request, "wishlist.html", context)
