from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Price(models.Model):
    price = models.FloatField()
    date = models.DateField()
    company_id = models.ForeignKey(Company, on_delete=models.PROTECT)
