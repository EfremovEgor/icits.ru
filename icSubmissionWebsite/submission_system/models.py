from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import validate_email


class PendingUser(models.Model):
    email = models.EmailField("Email", max_length=254)
    token = models.TextField("token", unique=True)
