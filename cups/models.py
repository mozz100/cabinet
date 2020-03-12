from django.db import models

class Trophy(models.Model):
    class Meta:
        verbose_name_plural = "trophies"

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name