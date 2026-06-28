from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def events(request):
    return render(request, 'events.html')

def event_details(request):
    return render(request, 'event_details.html')

def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html')

def my_events(request):
    return render(request, 'my_events.html')

def gallery(request):
    return render(request, 'gallery.html')

def notices(request):
    return render(request, 'notices.html')

def contact(request):
    return render(request, 'contact.html')
