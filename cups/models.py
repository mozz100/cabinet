from django.db import models

class Trophy(models.Model):
    name = models.CharField(max_length=100)
