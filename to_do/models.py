from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50)
    done = models.BooleanField(blank=False, null=False, default=False)
