from django.core.exceptions import ValidationError


# Enforce NAICS code as 5 digits
def validate_NAICS(naics):
    if len(naics) != 5:
        raise ValidationError('NAICS code must be 5 digits long')
    return True
