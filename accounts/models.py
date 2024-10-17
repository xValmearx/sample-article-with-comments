from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Our custome user model"""

    age = models.PositiveIntegerField(null=True, blank=True)
