from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Event
import uuid



def index(request):
    return HttpResponse("Welcome to home page")


def about(request):
    return HttpResponse("Welcome to about page")


def create_event(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        location = request.POST.get('location')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        Event.objects.create(
            id=uuid.uuid4(),
            name=name,
            description=description,
            location=location,
            start_date=start_date,
            end_date=end_date
        )

        return redirect('index')

    return render(request, 'base/create_event.html')


def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        event.name = request.POST.get('name')
        event.description = request.POST.get('description')
        event.location = request.POST.get('location')
        event.start_date = request.POST.get('start_date')
        event.end_date = request.POST.get('end_date')

        event.save()
        return redirect('index')

    return render(request, 'base/update_event.html', {'event': event})


def get_all_events(request):
    events = Event.objects.all()
    return render(request, 'base/home.html', {'events': events})


def get_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'base/event_detail.html', {'event': event})


def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('index')