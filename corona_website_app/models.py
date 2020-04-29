from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=200)
    num_cases = models.IntegerField()
    num_recoveries = models.IntegerField()
    num_deaths = models.IntegerField()

    def __str__(self):
        return self.name