import datetime

from django.core.management.base import BaseCommand
from myapp2.models import Product, Order, User


class Command(BaseCommand):
    help = "Generate fake orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            order = Order(customer=User.objects.get(id=i), date_ordered=(datetime.datetime.now() - datetime.timedelta(days=i+20)), total_price=100)
            order.save()
            order.products.add(Product.objects.get(id=i))
