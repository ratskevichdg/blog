from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_dealer = models.BooleanField(
        verbose_name="Is dealer",
        null=True,
    )
