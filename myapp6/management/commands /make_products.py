from random import choice, randint, uniform
from django.core.management.base import BaseCommand

from myapp2.models import Product


class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        products = []
        count = kwargs.get('count')
        for i in range(1, count + 1):
            products.append(Product(
                name=f'продукт номер {i}',
                description='длинное описание продукта, которое итак никто не читает',
                price=uniform(0.01, 999.99),
            ))
        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS(f'Сгенерировано {count} продуктов'))
