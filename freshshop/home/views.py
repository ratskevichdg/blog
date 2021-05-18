from django.shortcuts import render


def home(request):
    context = {"page_name": "home"}
    return render(request, "home.html", context)


def about(request):
    context = {"page_name": "about us"}
    return render(request, "about.html", context)


def contacts(request):
    context = {"page_name": "contacts"}
    return render(request, "contacts.html", context)


def gallery(request):
    context = {"page_name": "gallery"}
    return render(request, "gallery.html", context)
