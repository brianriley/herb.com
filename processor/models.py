from django.db import models


class Transaction(models.Model):
    posted = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)
