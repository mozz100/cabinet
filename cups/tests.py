from django.test import TestCase
from .models import Trophy

class TrophiesTestCase(TestCase):
    def test_trophy_creation(self):
        trophy = Trophy(name="European Cup", weight=5000)
        trophy.save()

        # Django wraps every test in a transaction
        self.assertEqual(1, Trophy.objects.count())

    def test_trophy_creation_independent(self):
        trophy = Trophy(name="Premier League", weight=4000)
        trophy.save()

        # No inter-dependent tests here
        self.assertEqual(1, Trophy.objects.count())
