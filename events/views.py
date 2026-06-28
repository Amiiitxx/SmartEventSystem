from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Registration
from .models import Event, UserProfile, Registration
import qrcode
from io import BytesIO
from django.http import HttpResponse
import qrcode
from io import BytesIO
from .forms import EventRegistrationForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# =========================
# HOME
# =========================

def home(request):

    events = Event.objects.all()[:4]

    return render(
        request,
        "home.html",
        {
            "events": events,
            "active_page": "home",
        },
    )


# =========================
# EVENTS
# =========================

from .models import Event, Registration

def events(request):

    query = request.GET.get("q")

    events = Event.objects.all()

    if query:
        events = events.filter(title__icontains=query)

    registered_event_ids = []

    if request.user.is_authenticated:
        registered_event_ids = Registration.objects.filter(
            user=request.user
        ).values_list("event_id", flat=True)

    return render(
        request,
        "events.html",
        {
            "events": events,
            "registered_event_ids": registered_event_ids,
            "active_page": "events",
            "query": query,
        },
    )
# =========================
# REGISTER EVENT
# =========================
@login_required(login_url="login")
def register_event(request, event_id):

    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":

        form = EventRegistrationForm(request.POST)

        if form.is_valid():

            Registration.objects.get_or_create(
                user=request.user,
                event=event
            )

            messages.success(
                request,
                "Event Registered Successfully!"
            )

            return redirect("my_events")

    else:

        form = EventRegistrationForm(
            initial={
                "full_name": request.user.get_full_name(),
                "email": request.user.email,
            }
        )

    return render(
        request,
        "register_event.html",
        {
            "form": form,
            "event": event,
        },
    )

# =========================
# MY EVENTS
# =========================

@login_required(login_url="login")
def my_events(request):

    registrations = Registration.objects.filter(
        user=request.user
    )

    return render(
        request,
        "my_events.html",
        {
            "registrations": registrations,
            "active_page": "my_events",
        },
    )

# =========================
# GALLERY
# =========================

def gallery(request):
    return render(request, "gallery.html", {"active_page": "gallery"})


# =========================
# NOTICES
# =========================

def notices(request):
    return render(request, "notices.html", {"active_page": "notices"})


# =========================
# CONTACT
# =========================

def contact(request):
    return render(request, "contact.html", {"active_page": "contact"})


# =========================
# RESULTS
# =========================

def results(request):
    return render(request, "results.html", {"active_page": "results"})


# =========================
# QR TICKET
# =========================

def ticket_qr(request):
    return render(request, "ticket_qr.html")


# =========================
# PROFILE
# =========================

from .models import Registration

@login_required(login_url="login")
def profile(request):

    profile_obj, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        uploaded_file = request.FILES.get("profile_pic")

        if uploaded_file:
            profile_obj.profile_pic = uploaded_file
            profile_obj.save()

    # User registered events
    registrations = Registration.objects.filter(
        user=request.user
    )

    registered_events = registrations.count()

    # One registration = One QR Ticket
    qr_tickets = registrations.count()

    # Future modules
    certificates = 0
    achievements = 0

    return render(
        request,
        "profile.html",
        {
            "profile": profile_obj,
            "registered_events": registered_events,
            "qr_tickets": qr_tickets,
            "certificates": certificates,
            "achievements": achievements,
        },
    )
# =========================
# LOGIN / REGISTER
# =========================

def login_page(request):

    if request.method == "POST":

        action = request.POST.get("action")

        if action == "login":

            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                return redirect("home")

            messages.error(request, "Invalid Username or Password")
            return redirect("login")

        elif action == "register":

            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect("login")

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return redirect("login")

            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            messages.success(
                request,
                "Registration Successful! Please Login."
            )

            return redirect("login")

    return render(request, "login.html")


# =========================
# LOGOUT
# =========================

def logout_view(request):
    logout(request)
    return redirect("home")

# =========================
# TICKET PAGE
# =========================

@login_required(login_url="login")
def ticket(request, registration_id):

    registration = get_object_or_404(
        Registration,
        id=registration_id,
        user=request.user
    )

    return render(
        request,
        "ticket.html",
        {
            "registration": registration
        }
    )


# =========================
# DOWNLOAD QR
# =========================

@login_required(login_url="login")
def download_qr(request, registration_id):

    registration = get_object_or_404(
        Registration,
        id=registration_id,
        user=request.user
    )

    qr_data = f"""
        Ticket ID : {registration.ticket_number}
        Student   : {registration.user.username}
        Event     : {registration.event.title}
        Date      : {registration.event.date}
        Venue     : {registration.event.venue}
    """

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=5,
        border=2
    )

    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    buffer = BytesIO()
    img.save(buffer, format="PNG")

    return HttpResponse(
        buffer.getvalue(),
        content_type="image/png"
    )

def event_details(request, event_id):

    event = get_object_or_404(
        Event,
        id=event_id
    )

    return render(
        request,
        "event_details.html",
        {
            "event": event
        }
    )