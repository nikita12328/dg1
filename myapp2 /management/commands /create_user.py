from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='John3', email='john@example2.com', password='secret2', age=25)
        user.save()
        self.stdout.write(f'{user}')
        user = User(name='Neo2', email='neo@example.com', password='secret', age=58)
        user.save()
        self.stdout.write(f'{user}')
