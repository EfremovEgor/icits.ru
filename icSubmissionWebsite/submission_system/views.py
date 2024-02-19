import json
from re import A
import secrets
import string
import uuid
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from icSubmissionWebsite import settings
from submission_system.models import (
    Contact,
    Submitter,
    Submission,
    Topic,
    SubmissionDetails,
    AuthorAffilation,
    SubmissionAuthorDetails,
    Abstract,
)
from .forms import CreateContactForm, LoginForm, RegistrationForm
from django.core.cache import cache
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView, UpdateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import schemas


def authentification_page(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy("submission_system:profile"))
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


def register_user(request):
    form = RegistrationForm(request.POST)
    if not form.is_valid():
        return HttpResponseRedirect("auth")
    submitter, created = Submitter.objects.get_or_create(
        email=form.cleaned_data["email"]
    )
    new_pass = ""
    if created:
        alphabet = string.ascii_letters + string.digits
        new_pass = "".join(secrets.choice(alphabet) for i in range(10))
        submitter.set_password(new_pass)
        submitter.save(update_fields=["password"])
    if new_pass or not submitter.is_active:
        token = uuid.uuid4().hex
        redis_key = settings.SUBMITTER_CONFIRMATION_KEY.format(token=token)
        cache.set(
            redis_key,
            {"submitter_id": submitter.id},
            timeout=settings.SUBMITTER_CONFIRMATION_TIMEOUT,
        )

        confirm_link = request.build_absolute_uri(
            reverse_lazy("submission_system:activate", kwargs={"token": token})
        )
        message = _(f"follow this link %s \n" f"to confirm! \n" % confirm_link)
        if new_pass:
            message += f"Your new password {new_pass} \n "
        send_mail(
            subject=_("Please confirm your registration!"),
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[
                submitter.email,
            ],
        )

        return render(
            request,
            "email_sent_success.html",
            {"message": f"Confirmation mail was sent to {submitter.email}"},
        )


def activate(request, token):
    redis_key = settings.SUBMITTER_CONFIRMATION_KEY.format(token=token)
    submitter_info = cache.get(redis_key) or {}
    if submitter_id := submitter_info.get("submitter_id"):
        submitter = get_object_or_404(Submitter, id=submitter_id)
        submitter.is_active = True
        submitter.save(update_fields=["is_active"])
        return HttpResponse("APPROVED")
    else:
        return HttpResponse("ERROR")


def login_user(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy("submission_system:profile"))

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get("next") is not None:
                    return redirect(request.GET.get("next"))
                return redirect(reverse_lazy("submission_system:profile"))
    return redirect(reverse_lazy("submission_system:auth_page"))


@login_required(login_url=reverse_lazy("submission_system:auth_page"))
def profile(request):
    return render(
        request,
        "profile/home.html",
        {
            "title": "Profile",
        },
    )


@login_required(login_url=reverse_lazy("submission_system:auth_page"))
def contact(request):
    contact = Contact.objects.filter(submitter__id=request.user.id).first()

    is_created = contact is not None
    if is_created:
        contact = {
            "Title": contact.title,
            "First Name": contact.first_name,
            "Last Name": contact.last_name,
            "Company/Institution": contact.company_or_institution,
            "Department": contact.department,
            "Email Address": contact.submitter.email,
            "Telephone Number": contact.phone_number,
            "Address": contact.contact_address,
            "City": contact.city,
            "ZIP/Postcode": contact.postcode,
            "Country": contact.country,
        }
    return render(
        request,
        "profile/contact.html",
        {
            "title": "Update Contact Information",
            "is_created": is_created,
            "contact": contact,
        },
    )


class CreateContactView(FormView, LoginRequiredMixin):
    form_class = CreateContactForm
    template_name = "profile/create_contact.html"
    success_url = reverse_lazy("submission_system:contact")

    def form_valid(self, form):
        contact = form.save(commit=False)
        submitter = Submitter.objects.get(id=self.request.user.id)
        if Contact.objects.filter(submitter=submitter).first() is not None:
            return render(
                self.request,
                "profile/message.html",
                {"title": "Error", "message": "Cannot create second contact"},
            )

        contact.submitter = submitter
        contact.save()
        return super().form_valid(form)


class EditContactView(UpdateView, LoginRequiredMixin):
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
    template_name = "profile/edit_contact.html"
    success_url = reverse_lazy("submission_system:contact")
    template_name_suffix = "_update_form"

    def get_object(self):
        return Contact.objects.filter(submitter__id=self.request.user.id).first()


def user_logout(request):
    logout(request)
    return redirect(reverse_lazy("submission_system:auth_page"))


class SubmitAbstractView(LoginRequiredMixin, View):
    template_name = "profile/submit_abstract.html"
    login_url = "submission_system:auth_page"

    def get(self, request):
        contact = Contact.objects.filter(submitter__id=request.user.id).first()

        return render(
            request,
            self.template_name,
            {
                "title": "Abstract Submission ",
                "contact": contact,
            },
        )

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            validate(data, schemas.abstract_schema)
        except ValidationError as ex:
            return JsonResponse(
                {
                    "status": 0,
                    "message": _(str(ex)),
                    "url": request.build_absolute_uri(
                        reverse_lazy("submission_system:profile")
                    ),
                }
            )
        submission = Submission(
            title=data["title"],
            presentation_type=data["presentation_type"],
            is_draft=False,
            submitter=Submitter.objects.get(id=self.request.user.id),
        )
        submission.save()
        topic = Topic(name=data["topic"])
        topic.save()
        submission_details = SubmissionDetails(
            submission=submission, topic=topic, bio=data["bio"]
        )
        submission_details.save()
        for author in data["authors"]:
            affilation = AuthorAffilation(
                affilation=author["affilation"]["affilation"],
                city=author["affilation"]["city"],
                state=author["affilation"]["state"],
                country=author["affilation"]["country"],
            )
            affilation.save()
            author_details = SubmissionAuthorDetails(
                submission_details=submission_details,
                title=author["title"],
                first_name=author["first_name"],
                last_name=author["last_name"],
                organization=author["organization"],
                is_presenter=author["is_presenter"],
                affilation=affilation,
            )
            author_details.save()
        abstract = Abstract(submission=submission, content=data["abstract"])
        abstract.save()

        return JsonResponse(
            {
                "status": 1,
                "message": _("Ok"),
                "url": request.build_absolute_uri(
                    reverse_lazy("submission_system:profile")
                ),
            }
        )
