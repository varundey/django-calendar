from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Event
from calendar_app.forms import EventForm
from datetime import datetime as dt
now=dt.now()
# Create your views here.

def index(request):
	if request.method=='POST':
		form = EventForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			form = EventForm()	
		else:
			print form.errors
	else:
		form = EventForm()
	return render(request, 'index.html', {"form":form})

def events(request):
	events = Event.objects.all()
	return HttpResponse(serialize("json", events))
	# return render(request, 'events.html', {'events':events})

def query(request):
	month = request.GET.get('month')
	year = request.GET.get('year')
	my_model_object = Event.objects.filter(start_date__month=month,
						start_date__year=year)
	obj_as_json = serialize("json", my_model_object)
	return HttpResponse(obj_as_json)