from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("submission_system.urls")),
    path("", include("information_pages.urls")),
]
