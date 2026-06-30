from django.urls import path
from . import views

urlpatterns = [

    # Home
    path('', views.home, name='home'),

    # Events
    path('events/', views.events, name='events'),
    path('event/<int:event_id>/', views.event_details, name='event_details'),

    # Registration
    path(
        'register/<int:event_id>/',
        views.register_event,
        name='register_event'
    ),

    # My Events
    path('my-events/', views.my_events, name='my_events'),

    # Ticket
    path(
        'ticket/<int:registration_id>/',
        views.ticket,
        name='ticket'
    ),

    path(
        'download-ticket/<int:registration_id>/',
        views.download_qr,
        name='download_qr'
    ),

    path('ticket/', views.ticket_qr, name='ticket_qr'),

    # Gallery
    path('gallery/', views.gallery, name='gallery'),

    # Results
    path('results/', views.results, name='results'),

    # Notices
    path('notices/', views.notices, name='notices'),

    # Contact
    path('contact/', views.contact, name='contact'),

    # Authentication
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Profile
    path('profile/', views.profile, name='profile'),

]