from django.db import models

class Trophy(models.Model):
    class Meta:
        verbose_name_plural = "trophies"

    name = models.CharField(max_length=100)
    weight = models.PositiveIntegerField(help_text="in g")

    def __str__(self):
        return self.name