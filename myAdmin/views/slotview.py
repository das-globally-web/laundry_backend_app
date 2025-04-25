# views.py

from django.shortcuts import render, redirect

from myAdmin.views.decorators import session_login_required
from .slotform import SlotForm
from slots.models import SlotTable
@session_login_required
def create_slot(request):
    if request.method == 'POST':
        form = SlotForm(request.POST)
        if form.is_valid():
            # Save to MongoDB using MongoEngine
            SlotTable(
                startTime=form.cleaned_data['startTime'],
                endtime=form.cleaned_data['endtime'],
                pickup=form.cleaned_data['pickup']
            ).save()
            return redirect('slot-list')  # or redirect to success page
    else:
        form = SlotForm()
    
    return render(request, 'slot_form.html', {'form': form})
@session_login_required
def list_slots(request):
    slots = SlotTable.objects.all()
    return render(request, 'slot_list.html', {'slots': slots})
