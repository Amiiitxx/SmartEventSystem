from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

from events.models import Event, Registration
from .forms import EventForm


# ==========================
# Dashboard
# ==========================

@staff_member_required(login_url="login")
def dashboard(request):

    total_events = Event.objects.count()

    total_registrations = Registration.objects.count()

    total_students = Registration.objects.values(
        "user"
    ).distinct().count()

    context = {
        "total_events": total_events,
        "total_registrations": total_registrations,
        "total_students": total_students,
    }

    return render(
        request,
        "adminpanel/dashboard.html",
        context
    )


# ==========================
# Add Event
# ==========================

@staff_member_required(login_url="login")
def add_event(request):

    if request.method == "POST":

        form = EventForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect("manage_events")

    else:

        form = EventForm()

    return render(
        request,
        "adminpanel/add_event.html",
        {
            "form": form
        }
    )


# ==========================
# Manage Events
# ==========================

@staff_member_required(login_url="login")
def manage_events(request):

    events = Event.objects.all()

    return render(
        request,
        "adminpanel/manage_events.html",
        {
            "events": events
        }
    )


# ==========================
# Students
# ==========================

@staff_member_required(login_url="login")
def students(request):

    registrations = Registration.objects.select_related(
        "user",
        "event"
    )

    return render(
        request,
        "adminpanel/students.html",
        {
            "registrations": registrations
        }
    )

# ==========================
# Delete Event
# ==========================

@staff_member_required(login_url="login")
def delete_event(request, event_id):

    event = get_object_or_404(
        Event,
        id=event_id
    )

    event.delete()

    return redirect("manage_events")


# ==========================
# Edit Event
# ==========================

@staff_member_required(login_url="login")
def edit_event(request, event_id):

    event = get_object_or_404(
        Event,
        id=event_id
    )

    if request.method == "POST":

        form = EventForm(
            request.POST,
            request.FILES,
            instance=event
        )

        if form.is_valid():

            form.save()

            return redirect("manage_events")

    else:

        form = EventForm(instance=event)

    return render(
        request,
        "adminpanel/add_event.html",
        {
            "form": form
        }
    )
