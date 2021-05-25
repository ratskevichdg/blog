from django import forms
from django.contrib.auth import authenticate
from django.forms import fields

from typing import Dict, Any
from user.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "name",
                "placeholder": "User Name",
                "data-error": "Please enter your name",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password",
                "placeholder": "Password",
                "data-error": "Please enter your password",
            }
        )
    )

    def clean(self):
        user = authenticate(**dict(self.cleaned_data))
        if user is not None:
            self.cleaned_data["user"] = user
            return self.cleaned_data
        else:
            self.add_error("username", "invalid username.")
            self.add_error("password", "or invalid password.")
            raise forms.ValidationError("User not found!")


class RegistrationForm(forms.ModelForm):
    password_repeat = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User

        fields = [
            "email",
            "username",
            "is_dealer",
            "password",
        ]
        widgets = {"password": forms.PasswordInput()}
    
    def save(self, commit: bool = False) -> Any:
        user = super().save(commit=commit)
        user.set_password(user.password)
        user.save()
        return user

    def clean(self) -> Dict[str, Any]:
        if self.cleaned_data["password"] != self.cleaned_data["password_repeat"]:
            # add error messages
            raise forms.ValidationError("Passwords doesn't match")
        return super().clean()
