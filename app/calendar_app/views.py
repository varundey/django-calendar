from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event
from django.core import serializers
from calendar_app.forms import EventForm

# Create your views here.

def index(request):
	if request.method=='POST':
		form = EventForm(request.POST)
		if form.is_valid():
			form.save()
			form = EventForm()
	else:
		form = EventForm()
	return render(request, 'index.html', {"form":form})

def events(request):
	events = Event.objects.all()
	return render(request, 'events.html', {'events':events})