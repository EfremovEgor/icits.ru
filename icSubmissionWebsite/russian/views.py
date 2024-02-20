from django.shortcuts import render


def home(request):
    return render(
        request,
        "russian/home.html",
        {
            "title": "Home",
        },
    )


def about(request):
    return render(
        request,
        "russian/about.html",
        {
            "title": "About",
        },
    )


def committee(request):
    return render(
        request,
        "russian/committee.html",
        {
            "title": "Committee",
        },
    )


def calendar_of_events(request):
    
    return render(
        request,
        "russian/calendar_of_events.html",
        {
            "title": "Calendar Of Events",
        },
    )


def abstract_submission(request):
    return render(
        request,
        "russian/abstract_submission.html",
        {
            "title": "Abstract Submission",
        },
    )


def venue(request):
    return render(
        request,
        "russian/venue.html",
        {
            "title": "Venue",
        },
    )


def accommodation(request):
    return render(
        request,
        "russian/accommodation.html",
        {
            "title": "Accommodation",
        },
    )


def contacts(request):
    return render(
        request,
        "russian/contacts.html",
        {
            "title": "Contacts",
        },
    )


def registration(request):
    return render(
        request,
        "russian/registration.html",
        {
            "title": "Registration",
        },
    )
