from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from submission_system.models import Contact, Submitter


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
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "type": "text",
                "autocomplete": "email",
            }
        ),
    )


class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "title",
            "first_name",
            "last_name",
            "company_or_institution",
            "department",
            "phone_number",
            "contact_address",
            "city",
            "postcode",
            "country",
        ]
