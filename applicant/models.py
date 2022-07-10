from django.db import models
from account.models import User


class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    education = models.CharField(max_length=254, null=True, blank=True)
