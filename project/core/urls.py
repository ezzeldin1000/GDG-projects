from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("events/create/", views.create_event, name="create_event"),
    path("events/<int:event_id>/update/", views.update_event, name="update_event"),
    path("events/", views.get_all_events, name="get_all_events"),
    path("events/<int:event_id>/", views.get_event, name="get_event"),
    path("events/<int:event_id>/delete/", views.delete_event, name="delete_event"),
]

