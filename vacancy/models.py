from django.db import models
from company.models import Company


class Vacancy(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    required_experience = models.IntegerField(null=True)
    salary = models.IntegerField(null=True)
    description = models.CharField(max_length=254)
