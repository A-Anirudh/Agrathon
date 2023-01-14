from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_farmer = models.BooleanField('Farmer', default=False)
    is_consumer = models.BooleanField('Consumer', default=False)

    def __str__(self):
      return self.username