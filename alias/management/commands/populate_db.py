import datetime as dt
from faker import Faker
from django.utils import timezone
from django.core.management.base import BaseCommand
from alias.models import Alias


fake = Faker()


class Command(BaseCommand):
    """This command will populate db with fake data"""

    def handle(self, *args, **options):
        self.stdout.write("Population db process...")
        for i in range(3):
            Alias.objects.create(alias=fake.name()[:10],
                                 target=fake.text()[:24],
                                 end=timezone.now() + dt.timedelta(days=i))
        self.stdout.write("Population db is done!!!")
