from django.urls import path
from . import views


urlpatterns = [
    path("submission_system/auth", views.authentification_page, name="auth_page"),
    path(
        "submission_system/auth/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/?P<token>[0-9A-Za-z_\-]+)/",
        views.activate,
        name="confirm",
    ),
    path(
        "submission_system/auth/create_pending_user",
        views.create_pending_user,
        name="create_pending_user",
    ),
]
