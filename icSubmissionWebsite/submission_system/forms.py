from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "type": "text",
                "autocomplete": "email",
            }
        ),
    )

    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input",
                "type": "password",
                "autocomplete": "off",
            }
        ),
    )


class RegistrationForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "type": "text",
                "autocomplete": "email",
            }
        ),
    )
    confirm_email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "type": "text",
            }
        ),
    )
