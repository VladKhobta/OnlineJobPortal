from django.core.exceptions import ValidationError


def validate_interval(value):
    if value < 1900 or value > 2022:
        raise ValidationError(
            'Year must be in 1900 to 2022',
            params={'value': value}
        )
