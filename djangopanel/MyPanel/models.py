from django.db import models
from django.utils.timezone import now

class Sale(models.Model):
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=now)  # Add default value for the date field

    def __str__(self):
        return self.product_name

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return self.project_name