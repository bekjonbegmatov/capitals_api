from django.db import models

# Create your models here.

class Countries(models.Model):
    country = models.CharField(max_length=256)
    capital = models.CharField(max_length=256)
    region = models.CharField(max_length=256)
    geography = models.TextField()

    def __str__(self):
        return self.country