from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from company.models import Company


def company_required(function):
    def is_company(u):
        return Company.objects.filter(user=u).exists()
    actual_decorator = user_passes_test(is_company)
    if function:
        return actual_decorator(function)
    else:
        return actual_decorator
