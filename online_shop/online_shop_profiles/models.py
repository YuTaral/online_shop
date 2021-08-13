from django.contrib.auth import get_user_model
from django.db import models

from core.validators import length_validator, first_letter_uppercase_validator

UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank=True,
        validators=[length_validator, first_letter_uppercase_validator]
    )
    last_name = models.CharField(
        max_length=20,
        blank=True,
        validators=[length_validator, first_letter_uppercase_validator]
    )
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    profile_image = models.FileField(
        upload_to='profiles',
        blank=True,
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    is_complete = models.BooleanField(
        default=False,
    )


