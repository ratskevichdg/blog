from django.shortcuts import redirect, render, HttpResponseRedirect
from django.urls.base import reverse
from django.contrib.auth import login as log_in, logout as log_out
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views import View
from user.forms import LoginForm, RegistrationForm


def login(request):
    if not request.user.is_anonymous:
        return redirect(reverse("home_page"))
    context = {"login_form": LoginForm()}
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            log_in(request, login_form.cleaned_data["user"])
            return redirect(reverse("home_page"))
        else:
            context["login_form"] = login_form
    return render(request, "login.html", context)


@login_required(login_url="login_page")
def logout(request):
    log_out(request)
    return redirect(reverse("home_page"))

# class Registration(TemplateView):
#     template_name = "registration.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update(registration_form = RegistartionForm())
#         return context

class Registration(View):
    form_class = RegistrationForm
    template_name = "registration.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context.update(registration_form = self.form_class())
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("login_page"))
        self.context.update(registration_form=form)
        return render(request, self.template_name, self.context)

