from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashboard, name='admin_dashboard'),

    path('add-event/', views.add_event, name='add_event'),

    path('manage-events/', views.manage_events, name='manage_events'),

    path('students/', views.students, name='students'),

    path(
        'delete-event/<int:event_id>/',
        views.delete_event,
        name='delete_event'
    ),

    path(
        'edit-event/<int:event_id>/',
        views.edit_event,
        name='edit_event'
    ),
]