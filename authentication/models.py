from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    speciality = models.CharField(max_length=20, default="Psychiatry")


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.user.first_name
