from django.db import models
from account.models import User
from utilities.validators import validate_interval


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    designation = models.CharField(max_length=254, null=True, blank=True)
    description = models.CharField(max_length=254, null=True, blank=True)
    establishment_date = models.IntegerField(validators=[validate_interval], null=True, blank=True)


class BusinessStream(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE, primary_key=True)

    class Types(models.TextChoices):
        IT = 'IT', 'It'
        PETROLEUM = 'PETROLEUM', 'Petroleum'
        TOURISM = 'TOURISM', 'Tourism'

    base_type = Types.IT
    type = models.CharField(max_length=50, choices=Types.choices, default=base_type)
