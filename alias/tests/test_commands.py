from django.core.management import call_command
from django.test import TestCase
from alias.models import Alias


class CommandTest(TestCase):
    """This class contain all tests for custom user commands"""

    def test_population_db(self):
        """Testing population db command"""

        call_command('populate_db')
        alias = Alias.objects.all()

        self.assertIsNotNone(alias)
        self.assertEqual(3, len(alias))
        self.assertIsNotNone(alias[0].alias)
