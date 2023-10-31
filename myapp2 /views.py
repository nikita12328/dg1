import datetime

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils import timezone

from myapp2.models import Order, User


def get_orders_by_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer=user)
    return render(request, 'myapp2/order_list.html', {'orders': orders})


def get_orders_last_7_days(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer=user, date_ordered__gt=(timezone.now() - datetime.timedelta(days=7)))
    return render(request, 'myapp2/order_list.html', {'orders': orders})


def get_orders_last_30_days(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer=user, date_ordered__gt=(timezone.now() - datetime.timedelta(days=30)))
    return render(request, 'myapp2/order_list.html', {'orders': orders})


def get_orders_last_year(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer=user, date_ordered__gt=(timezone.now() - datetime.timedelta(days=365)))
    return render(request, 'myapp2/order_list.html', {'orders': orders})
