from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # path(
    #     "submission/", include("submission_system.urls", namespace="submission_system")
    # ),
    path("en/", include("information_pages.urls")),
    path("", include("russian.urls")),

]
