from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("abstract-submission", views.abstract_submission, name="abstract_submission"),
    path("accommodation", views.accommodation, name="accommodation"),
    path("calendar-of-events", views.calendar_of_events, name="calendar_of_events"),
    path("committee", views.committee, name="committee"),
    path("contacts", views.contacts, name="contacts"),
    path("registration", views.registration, name="registration"),
    path("venue", views.venue, name="venue"),
]
