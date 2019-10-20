from django.contrib.auth.models import User
from django.db import models

# Create your models here.
"""
class UserDonor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mail = models.CharField()
    def __str__(self):
        return self.user.username

class UserDonated(models.Model):
    user = user = models.OneToOneField(User, on_delete=models.CASCADE)
"""

# class ClimaticEvent(models.Model):
#    event_time = models.DateField()