import json
import secrets
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .forms import LoginForm, RegistrationForm
from .models import PendingUser
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


def authentification_page(request):
    login_form = LoginForm()
    registration_form = RegistrationForm()
    return render(
        request,
        "auth.html",
        {
            "title": "Auth",
            "login_form": login_form,
            "registration_form": registration_form,
        },
    )


def create_pending_user(request):
    data = json.loads(request.body)

    email = data.get("email")
    if (
        PendingUser.objects.filter(email=email).exists()
        or User.objects.filter(email=email).exists()
    ):
        return JsonResponse({"result": "error", "message": "user already exists"})
    pending_user = PendingUser(email=email, token=secrets.token_urlsafe(20))
    pending_user.save()
    return JsonResponse({"result": "ok"})


def activate(request, uidb64, token):
    print(1)
    return JsonResponse({"result": "ok"})
