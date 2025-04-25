

from django.shortcuts import render
from myAdmin.views.decorators import session_login_required
from orders.models import OrderTable
@session_login_required
def allOrders(request):
  # Replace with your model
    products = OrderTable.objects.all().order_by('-id')  # MongoEngine query
    return render(request, 'allorders.html', {'orders': products})
