from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = "submission_system"

urlpatterns = [
    path("auth", views.authentification_page, name="auth_page"),
    path("register", views.register_user, name="register_user"),
    path("login", views.login_user, name="login_user"),
    path("activate/<token>/", views.activate, name="activate"),
    path("profile", views.profile, name="profile"),
    path("contact", views.contact, name="contact"),
    path(
        "contact/create/",
        login_required(views.CreateContactView.as_view()),
        name="create_contact",
    ),
    path(
        "contact/edit/",
        login_required(views.EditContactView.as_view()),
        name="edit_contact",
    ),
    path("logout", views.user_logout, name="logout_user"),
    path("abstract/submit", views.submit_abstract, name="submit_abstract"),
]
