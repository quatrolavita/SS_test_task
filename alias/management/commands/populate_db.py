import datetime as dt
from faker import Faker
from django.utils import timezone
from django.core.management.base import BaseCommand
from alias.models import Alias

class Command(BaseCommand):
    """This class will enable command, that will populate db with fake data"""

    def handle(self, *args, **options):
        """This method will handle all job for command

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        self.stdout.write("Population db process...")
        fake = Faker()
        for i in range(3):
            Alias.objects.create(alias=fake.name()[:10],
                                 target=fake.text()[:24],
                                 end=timezone.now() + dt.timedelta(days=i))
        self.stdout.write("Population db is done!!!")
