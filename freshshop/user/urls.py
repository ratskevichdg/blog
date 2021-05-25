from django.urls import path
from . import views as user
from django.urls import reverse
from django.shortcuts import redirect

urlpatterns = [
    path("login/", user.login, name="login_page"),
    path("logout/", user.logout, name="logout_page"),
    path("signin/", user.Registration.as_view(), name="signin_page"),
    path("", lambda request: redirect(reverse("login_page"))),
]
