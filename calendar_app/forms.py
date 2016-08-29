from django.forms import ModelForm
from calendar_app.models import Event

class EventForm(ModelForm):

	class Meta:
		model = Event
		fields='__all__'

