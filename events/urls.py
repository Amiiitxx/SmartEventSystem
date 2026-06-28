from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('events/', views.events, name='events'),

    path(
        'register/<int:event_id>/',
        views.register_event,
        name='register_event'
    ),

    path('my-events/', views.my_events, name='my_events'),

    path('results/', views.results, name='results'),
    path('gallery/', views.gallery, name='gallery'),
    path('notices/', views.notices, name='notices'),
    path('contact/', views.contact, name='contact'),

    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('profile/', views.profile, name='profile'),
    path('ticket/', views.ticket_qr, name='ticket_qr'),

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
    path(
    'event/<int:event_id>/',
    views.event_details,
    name='event_details'
),
]

