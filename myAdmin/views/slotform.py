# slotform.py
from django import forms

class SlotForm(forms.Form):
    startTime = forms.CharField(max_length=100, label="Start Time")
    endtime = forms.CharField(max_length=100, label="End Time")
    pickup = forms.BooleanField(required=False, label="Pickup Available")
