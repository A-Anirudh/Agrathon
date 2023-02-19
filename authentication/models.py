from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
    (1, 'Farmer'),
    (2, 'Consumer'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,blank=True,null=True)

    def __str__(self):
      return self.username