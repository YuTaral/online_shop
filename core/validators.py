from django.core.exceptions import ValidationError


def first_letter_uppercase_validator(value):
    if value[0].islower():
        raise ValidationError(f'This value "{value}" should starts with uppercase.')
