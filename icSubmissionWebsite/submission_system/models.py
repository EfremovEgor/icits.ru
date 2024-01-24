from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Submitter(AbstractUser):
    username = models.CharField(
        _("username"),
        max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
        validators=[AbstractUser.username_validator],
        null=True,
        blank=True,
    )
    email = models.EmailField(
        _("email address"),
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
        unique=True,
    )
    is_active = models.BooleanField(
        _("active"),
        default=False,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Contact(models.Model):
    submitter = models.OneToOneField(Submitter, on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=200, null=False, blank=False)
    first_name = models.CharField(
        _("First Name"),
        max_length=200,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        _("First Name"),
        max_length=200,
        null=False,
        blank=False,
    )
    company_or_institution = models.CharField(
        _("Company/Institution"),
        max_length=200,
        null=False,
        blank=False,
    )
    department = models.CharField(
        _("Department"),
        max_length=200,
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        _("Phone Number"),
        max_length=200,
        null=True,
        blank=True,
    )

    contact_address = models.TextField(
        _("Contact Address"),
        null=False,
        blank=False,
    )
    city = models.CharField(
        _("City"),
        max_length=200,
        null=False,
        blank=False,
    )
    postcode = models.CharField(
        _("ZIP/Postcode"),
        max_length=200,
        null=True,
        blank=True,
    )
    country = models.CharField(
        _("country"),
        max_length=200,
        null=False,
        blank=False,
    )


class Submission(models.Model):
    PRESENTATION_TYPE_CHOICES = (
        ("online", "Online"),
        ("offline", "Offline"),
    )
    title = models.TextField(_("Title"))
    presentation_type = models.CharField(
        max_length=300, choices=PRESENTATION_TYPE_CHOICES
    )
    is_draft = models.BooleanField(_("Draft"), default=True)


class Topic(models.Model):
    name = models.CharField(_("Name"), max_length=250)


class SubmissionDetails(models.Model):
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)


class AuthorAffilation(models.Model):
    affilation = models.CharField(_("Affilation"), max_length=255)
    city = models.CharField(_("City/Suburb/Town"), max_length=255)
    state = models.CharField(_("State"), max_length=255, null=True, blank=True)
    country = models.CharField(_("Country"), max_length=255)


class SubmissionAuthorDetails(models.Model):
    submission_details = models.ForeignKey(SubmissionDetails, on_delete=models.CASCADE)
    affilation = models.ForeignKey(
        AuthorAffilation, on_delete=models.SET_NULL, null=True
    )
    title = models.CharField(_("Title"), max_length=255)
    first_name = models.CharField(_("First Name"), max_length=255)
    last_name = models.CharField(_("Last Name"), max_length=255)
    organization = models.CharField(_("Last Name"), max_length=255)
    is_presenter = models.BooleanField(_("Presenter"))


class Abstract(models.Model):
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE)
    content = models.TextField(_("Content"))
