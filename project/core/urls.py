from django.urls import path

from . import views
import uuid

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("events/create/", views.create_event, name="create_event"),
    path("events/<uuid:event_id>/update/", views.update_event, name="update_event"),
    path("events/", views.get_all_events, name="get_all_events"),
    path("events/<uuid:event_id>/", views.get_event, name="get_event"),
    path("events/<uuid:event_id>/delete/", views.delete_event, name="delete_event"),
]

