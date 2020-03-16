from django.db import models


class Usage(models.Model):
    date = models.DateTimeField()
    amount = models.FloatField()
    type = models.CharField(max_length=150)