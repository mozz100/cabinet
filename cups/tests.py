from django.test import TestCase
# from django.urls import reverse
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


class TrophiesAPITestCase(TestCase):
    def test_list_trophies(self):
        trophy = Trophy.objects.create(name="FA Cup", weight=3000)
        response = self.client.get("/api/v1/trophies/")
        self.assertEqual(200, response.status_code)

        data = response.json()
        self.assertEqual(1, len(data))
        self.assertEqual(trophy.name, data[0]["name"])

    def test_create_trophy(self):
        response = self.client.post("/api/v1/trophies/",
            content_type="application/json",
            data={
                "name": "League Cup",
                "weight": 1234,
            }
        )
        self.assertEqual(201, response.status_code)
        self.assertEqual(1, Trophy.objects.count())
