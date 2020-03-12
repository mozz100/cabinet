from django.db import models

class Trophy(models.Model):
    class Meta:
        verbose_name_plural = "trophies"

    name = models.CharField(max_length=100)
    weight = models.PositiveIntegerField(help_text="in g")

    def __str__(self):
        return self.name

class Season(models.Model):
    year = models.PositiveIntegerField()
    trophies = models.ManyToManyField(Trophy)

class Story(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
