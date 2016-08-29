from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models
from django.forms import ModelForm
from datetime import timedelta as td
from datetime import time as t
from datetime import datetime as dt

time={21:1, 22:2, 23:3}
now=dt.now()
class Event(models.Model):
	
	event_name = models.CharField(max_length=20)
	
	location = models.CharField(blank=True, max_length=50)
	
	start_date = models.DateField(default = now.date() )
	
	start_time = models.TimeField(default = t(now.hour, now.minute, now.second) )

	all_day = models.BooleanField(default=False)
	
	description = models.CharField(blank = True, max_length=200)
	
	if now.hour<=20:
		end_time = models.TimeField(default = t(now.hour+3, now.minute, now.second) )
		end_date = models.DateField(default = now.date() )
	else:
		end_time = models.TimeField(default = t(time[now.hour], now.minute, now.second) )
		end_date = models.DateField(default = now.date() + td(days=1) )

	def __str__(self):
		return self.event_name

	def save(self, *args, **kwargs):
		if self.all_day==True:
			self.start_time = t(0,0,0)
			self.end_time = t(23,59,59)
			self.end_date = self.start_date

		if self.end_date < self.start_date:
			raise ValidationError('Check that your end date is greater than start date!')
		elif self.start_date == self.end_date:
			if self.start_time >= self.end_time:
				raise ValidationError('Check that your end time is greater than start time!')

		super(Event, self).save(*args, **kwargs)
