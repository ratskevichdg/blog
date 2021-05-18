from django.urls import path
from . import views as home
from django.urls import reverse
from django.shortcuts import redirect

urlpatterns = [
    path("home/", home.home, name="home_page"),
    path("about/", home.about, name="about_us"),
    path("contacts/", home.contacts, name="contacts"),
    path("gallery/", home.gallery, name="gallery"),
    path("", lambda request: redirect(reverse("home_page"))),
]