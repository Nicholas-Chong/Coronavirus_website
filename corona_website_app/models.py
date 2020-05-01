from django.db import models
from django.contrib.postgres.fields import ArrayField

class Country(models.Model):
    name = models.CharField(max_length=200)
    num_cases = models.IntegerField()
    num_recoveries = models.IntegerField()
    num_deaths = models.IntegerField()

    daily_confirmed_cases = ArrayField(ArrayField(models.CharField(blank=True, max_length=50)))

    def __str__(self):
        return self.name