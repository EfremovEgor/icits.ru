from django.shortcuts import render


def home(request):
    return render(
        request,
        "information_pages/home.html",
        {
            "title": "Home",
        },
    )


def about(request):
    return render(
        request,
        "information_pages/about.html",
        {
            "title": "About",
        },
    )


def committee(request):
    return render(
        request,
        "information_pages/committee.html",
        {
            "title": "Committee",
        },
    )


def calendar_of_events(request):
    return render(
        request,
        "information_pages/calendar_of_events.html",
        {
            "title": "Calendar Of Events",
        },
    )


def abstract_submission(request):
    return render(
        request,
        "information_pages/abstract_submission.html",
        {
            "title": "Abstract Submission",
        },
    )


def venue(request):
    return render(
        request,
        "information_pages/venue.html",
        {
            "title": "Venue",
        },
    )


def accommodation(request):
    return render(
        request,
        "information_pages/accommodation.html",
        {
            "title": "Accommodation",
        },
    )


def contacts(request):
    return render(
        request,
        "information_pages/contacts.html",
        {
            "title": "Contacts",
        },
    )


def registration(request):
    return render(
        request,
        "information_pages/registration.html",
        {
            "title": "Registration",
        },
    )
