from django.core.management.base import BaseCommand
from myapp2.models import Product, Order, User


class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(name=f'Product_{i}', price=f'{i}', description=f'Text from {i} is bla bla bla many long text', image=f'products/{i}.jpg')
            product.save()
